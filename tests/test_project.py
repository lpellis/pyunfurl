#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pyunfurl


class UnitTests(unittest.TestCase):
    def test_import(self):
        self.assertIsNotNone(pyunfurl)

    def test_custom_embed(self):
        custom = pyunfurl.custom_unfurl(
            "https://news.ycombinator.com/item?id=16319505", 15
        )
        self.assertEqual(
            "https://news.ycombinator.com/favicon.ico",
            custom["favicon"],
            "custom:favicon",
        )
        self.assertEqual(
            "https://news.ycombinator.com/item?id=16319505", custom["url"], "custom:url"
        )
        self.assertEqual(
            "SpaceX’s Falcon Heavy successfully launches",
            custom["title"],
            "custom:title",
        )
        self.assertEqual("", custom["description"], "custom:description")

        custom = pyunfurl.custom_unfurl(
            "https://news.ycombinator.com/item?id=16319522", 15
        )
        self.assertEqual(
            "https://news.ycombinator.com/favicon.ico",
            custom["favicon"],
            "custom:favicon",
        )
        self.assertEqual(
            "https://news.ycombinator.com/item?id=16319522", custom["url"], "custom:url"
        )
        self.assertEqual(
            "SpaceX’s Falcon Heavy successfully launches",
            custom["title"],
            "custom:title",
        )
        self.assertEqual("There was something doubly awesome about the two falcons landing at the same time right next to each other!", custom["description"], "custom:description")

    def test_oembed(self):
        oembed = pyunfurl.oembed("https://www.youtube.com/watch?v=v-eK_cpTsOw", 15)
        self.assertEqual(
            "https://www.youtube.com/", oembed["provider_url"], "oembed:provider_url"
        )
        self.assertEqual(
            "https://www.youtube.com/watch?v=v-eK_cpTsOw", oembed["url"], "oembed:url"
        )
        self.assertEqual(
            "Adam Savage Answers: What's the Scariest Experience You've Had on Mythbusters?",
            oembed["title"],
            "oembed:title",
        )
        self.assertEqual("YouTube", oembed["provider_name"], "oembed:provider_name")
        self.assertEqual("video", oembed["type"], "oembed:type")
        self.assertEqual(
            "https://i.ytimg.com/vi/v-eK_cpTsOw/hqdefault.jpg",
            oembed["thumbnail_url"],
            "oembed:thumbnail_url",
        )
        self.assertEqual(270, oembed["height"], "oembed:height")
        self.assertEqual(
            "Adam Savage’s Tested", oembed["author_name"], "oembed:author_name"
        )
        self.assertEqual(
            '<iframe width="480" height="270" src="https://www.youtube.com/embed/v-eK_cpTsOw?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            oembed["html"],
            "oembed:html",
        )

    def test_open_graph(self):
        html = """
                <meta property='og:type' content="video.movie" />
                <meta property='fb:app_id' content='115109575169727' />
                <link rel='image_src' href="https://wrong.png">
                <meta property='og:image' content="https://m.media-amazon.com/images/M/MV5BZDJjOTE0N2EtMmRlZS00NzU0LWE0ZWQtM2Q3MWMxNjcwZjBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY1200_CR90,0,630,1200_AL_.jpg" />
                <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
                <meta property='og:title' content="The Rock (1996) - IMDb" />
                <meta property='og:site_name' content='IMDb' />
                <meta name="title" content="The Rock (1996) - IMDb" />
                <meta property="og:description" content="Directed by Michael Bay.  With Sean Connery, Nicolas Cage, Ed Harris, John Spencer" />
                <meta name="keywords" content="Reviews, Showtimes, DVDs, Photos, Message Boards, User Ratings, Synopsis, Trailers, Credits" />
        """
        og = pyunfurl.open_graph(
            "https://www.imdb.com/title/tt0117500/?q=none", 15, html
        )
        self.assertEqual(
            "https://m.media-amazon.com/images/M/MV5BZDJjOTE0N2EtMmRlZS00NzU0LWE0ZWQtM2Q3MWMxNjcwZjBhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
            og["image"],
            "og:image",
        )
        self.assertEqual("http://www.imdb.com/title/tt0117500/", og["url"], "og:url")
        self.assertEqual("The Rock (1996) - IMDb", og["title"], "og:title")
        self.assertEqual("IMDb", og["site_name"], "og:site_name")
        self.assertEqual("video.movie", og["type"], "og:type")
        self.assertEqual(
            "Directed by Michael Bay.  With Sean Connery, Nicolas Cage, Ed Harris, John Spencer",
            og["description"],
            "og:description",
        )

    def test_twitter_card(self):
        html = """
            <meta name="twitter:card" content="summary_large_image">
            <meta name="twitter:site" content="@smallbiztrends">
            <meta name="twitter:url" content="https://smallbiztrends.com/2015/10/what-are-twitter-cards-for-business.html">
            <meta name="twitter:title" content="What Are Twitter Cards and How Do I Use Them?">
            <meta name="twitter:creator" content="@mattsmansfield">
            <meta name="twitter:image" content="https://smallbiztrends.com/wp-content/uploads/2015/10/what-are-twitter-cards-for-business.jpg">
            <meta name="twitter:description" content="One of the biggest shortcomings of Twitter has always been its 140 character per tweet limit.">
        """
        card = pyunfurl.twitter_card(
            "https://smallbiztrends.com/2015/10/what-are-twitter-cards-for-business.html?q=none",
            15,
            html,
        )
        self.assertEqual(
            "https://smallbiztrends.com/wp-content/uploads/2015/10/what-are-twitter-cards-for-business.jpg",
            card["image"],
            "card:image",
        )
        self.assertEqual(
            "https://smallbiztrends.com/2015/10/what-are-twitter-cards-for-business.html",
            card["url"],
            "card:url",
        )
        self.assertEqual(
            "What Are Twitter Cards and How Do I Use Them?", card["title"], "card:title"
        )
        self.assertEqual("@smallbiztrends", card["site_name"], "card:site_name")
        self.assertEqual("@mattsmansfield", card["creator"], "card:type")
        self.assertEqual(
            "One of the biggest shortcomings of Twitter has always been its 140 character per tweet limit.",
            card["description"],
            "card:description",
        )

    def test_meta_tags(self):
        html = """
            <link rel="shortcut icon" href="myfavicon.ico">
            <meta name="description" content="Test description meta">
            <meta name="title" content="Title for meta">
            <meta name="url" content="https://example.com/article.html">
            <meta name="image" content="https://example.com/wp-content/uploads/2015/10/some-img.jpg">
            <meta name="keywords" content="Programming, Writing">
        """
        meta = pyunfurl.meta_tags("https://example.com/article.html?q=none", 15, html)
        self.assertEqual(
            "https://example.com/wp-content/uploads/2015/10/some-img.jpg",
            meta["image"],
            "meta:image",
        )
        self.assertEqual("https://example.com/article.html", meta["url"], "meta:url")
        self.assertEqual("Title for meta", meta["title"], "meta:title")
        self.assertEqual("myfavicon.ico", meta["favicon"], "meta:favicon")
        self.assertEqual(
            "Test description meta", meta["description"], "card:description"
        )
