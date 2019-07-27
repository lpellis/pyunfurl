import requests
from uritools import urisplit


def hackernews(url, timeout=15, html=None):
    """Returns the comment text and story title.  Domain is prefixed with the submitter/commenter name"""

    id = urisplit(url).getquerydict().get("id")[0]
    item = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{id}.json", timeout=timeout
    ).json()

    text = ""
    if "text" in item:
        text = item["text"]

    title = ""
    root_item = item
    # find the root submitted post to get the title
    while 1:
        if "title" in root_item:
            title = root_item["title"]
            break
        if "parent" in root_item:
            root_item = requests.get(
                f"https://hacker-news.firebaseio.com/v0/item/{root_item['parent']}.json",
                timeout=timeout,
            ).json()
        else:
            break

    if "title" in item:
        title = item["title"]

    return {
        "url": url,
        "title": title,
        "site_name": f"{item['by']} (news.ycombinator.com)",
        "description": text,
        "image": "",
        "favicon": "https://news.ycombinator.com/favicon.ico",
    }


CUSTOM_PROVIDER_LIST = [[r"https://news\.ycombinator\.com/item\?id=[0-9]+", hackernews]]
