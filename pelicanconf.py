#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Enda Farrell"
SITENAME = "endafarrell.net"
SITEURL = ""

# These two need to go together and be consistent!
ARTICLE_URL = "posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/index.html"

PATH = "content"

TIMEZONE = "Europe/Berlin"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# MARKDOWN = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra']

# Blogroll - Not used
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget - Not used
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = 100

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Adds jupyter notebooks to the file-types recognised as containing markup.
# @see https://github.com/danielfrg/pelican-ipynb
MARKUP = ("md", "ipynb")

# Adds the pelican-ipynb plugin
PLUGIN_PATHS = ["./plugins", "pelican-plugins"]
PLUGINS = ["ipynb.markup", "assets"]
IGNORE_FILES = [".ipynb_checkpoints"]

GOOGLE_ANALYTICS = "UA-101964846-1"
