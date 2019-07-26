#!/usr/bin/env python
# -*- coding: utf-8 -*-
from micawber import Provider, ProviderRegistry, ProviderException

__version__ = "0.0.0.1"
import micawber
import requests
from pyquery import PyQuery as pq
from uritools import urijoin


def wrap_response(url, data, method):

    title = ("title" in data and data["title"]) or ""
    image = ("image" in data and data["image"]) or ""
    favicon = ("favicon" in data and data["favicon"]) or ""
    description = ("description" in data and data["description"]) or ""
    url = ("url" in data and data["url"]) or url
    css = ("css" in data and data["css"]) or ""

    if image:
        image = urijoin(url, image)

    if favicon:
        favicon = urijoin(url, favicon)

    site = data["title"]
    if "site_name" in data and data["site_name"]:
        site = data["site_name"]
    if "provider_name" in data and data["provider_name"]:
        site = data["provider_name"]

    if method == "oembed" or method == "custom":
        html = data["html"]
    else:
        if image:
            html = f"""<div class="unfurl unfurl-image"><a rel="noopener nofollow" target="_blank" href="{url}"><img src="{image}"></a>
            <div class="unfurl-site">{site}</div>
            <div class="unfurl-title"><a rel="noopener nofollow" target="_blank" href="{url}">{title}</a></div>
            <div class="unfurl-description">{description}</div></div>"""
        elif favicon:
            html = f"""<div class="unfurl unfurl-image unfurl-favicon"><a rel="noopener nofollow" target="_blank" href="{url}"><img src="{favicon}"></a>
            <div class="unfurl-site">{site}</div>
            <div class="unfurl-title"><a rel="noopener nofollow" target="_blank" href="{url}">{title}</a></div>
            <div class="unfurl-description">{description}</div></div>"""
        else:
            html = f"""<div class="unfurl unfurl-plain">
            <div class="unfurl-site">{site}</div>
            <div class="unfurl-title"><a rel="noopener nofollow" target="_blank" href="{url}">{title}</a></div>
            <div class="unfurl-description">{description}</div></div>"""

    return {
        "method": method,
        "site": site,
        "title": title,
        "description": description,
        "image": image,
        "favicon": favicon,
        "url": url,
        "type": "rich",
        "html": html,
        "css": css,
    }


def updated_provider_list():
    providers = [[entry[0], entry[1].endpoint] for entry in micawber.bootstrap_basic()]
    providers.extend(
        [[entry[0], entry[1].endpoint] for entry in micawber.bootstrap_oembed()]
    )
    providers.extend(
        [[entry[0], entry[1].endpoint] for entry in micawber.bootstrap_noembed()]
    )
    # print(json.dumps(providers))

    return providers


def load_provider():
    provider = ProviderRegistry(None)
    for entry in updated_provider_list():
        provider.register(entry[0], Provider(entry[1]))

    return provider


# https://medium.com/slack-developer-blog/everything-you-ever-wanted-to-know-about-unfurling-but-were-afraid-to-ask-or-how-to-make-your-e64b4bb9254


def open_graph(url, timeout=15, html=None):

    if not html:
        html = requests.get(url, timeout=timeout).text

    d = pq(html)
    return {
        "type": d('meta[property="og:type"]').attr("content"),
        "url": d('meta[property="og:url"]').attr("content"),
        "title": d('meta[property="og:title"]').attr("content"),
        "site_name": d('meta[property="og:site_name"]').attr("content"),
        "description": d('meta[property="og:description"]').attr("content"),
        "image": d('meta[property="og:image"]').attr("content"),
        "audio": d('meta[property="og:audio"]').attr("content"),
        "locale": d('meta[property="og:locale"]').attr("content"),
        "video": d('meta[property="og:video"]').attr("content"),
    }


def twitter_card(url, timeout=15, html=None):

    if not html:
        html = requests.get(url, timeout=timeout).text

    d = pq(html)
    return {
        "card": d('meta[name="twitter:card"]').attr("content"),
        "url": d('meta[name="twitter:url"]').attr("content"),
        "site_name": d('meta[name="twitter:site"]').attr("content"),
        "creator": d('meta[name="twitter:creator"]').attr("content"),
        "description": d('meta[name="twitter:description"]').attr("content"),
        "image": d('meta[name="twitter:image"]').attr("content"),
        "title": d('meta[name="twitter:title"]').attr("content"),
    }


def meta_tags(url, timeout=15, html=None):
    if not html:
        html = requests.get(url, timeout=timeout).text

    d = pq(html)
    favicon = d('link[rel="shortcut icon"]').attr("href")
    if not favicon:
        favicon_url = urijoin(url, "/favicon.ico")
        r = requests.head(favicon_url)
        if r.status_code == 200:
            favicon = favicon_url

    return {
        "title": d('meta[name="title"]').attr("content") or d("title").text(),
        "description": d('meta[name="description"]').attr("content"),
        "image": d('meta[name="image"]').attr("content"),
        "favicon": favicon,
        "url": d('meta[name="canonical"]').attr("content")
        or d('meta[name="url"]').attr("content"),
        "keywords": d('meta[name="keywords"]').attr("content"),
    }


def oembed(url, timeout=15, html=None):
    embed = None
    try:
        return load_provider().request(url)
    except ProviderException:
        pass

    if not embed:
        try:
            if not html:
                html = requests.get(url, timeout=timeout).text

            d = pq(html)
            oembed_url = d('link[type="application/json+oembed"]').attr("href")
            if oembed_url:
                return requests.get(oembed_url, timeout=timeout).json()
        except requests.exceptions.RequestException as e:
            return None

    return None


def extend_dict(d1, d2):
    result = d2.copy()
    result.update({k: v for k, v in d1.items() if v})
    return result


def completed(data):
    return data["title"] and data["description"] and data["image"] and data["url"]


def unfurl(url, timeout=15, html=None):

    data = oembed(url, timeout, html)
    if data:
        return wrap_response(url, data, "oembed")

    data = twitter_card(url, timeout, html)
    if completed(data):
        return wrap_response(url, data, "twitter_card")

    data = extend_dict(data, open_graph(url, timeout, html))
    if completed(data):
        return wrap_response(url, data, "open_graph")

    data = extend_dict(data, meta_tags(url, timeout, html))
    return wrap_response(url, data, "meta_tags")


if __name__ == "__main__":
    print(unfurl("https://news.ycombinator.com/item?id=20508465"))
