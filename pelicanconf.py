# -*- coding: utf-8 -*- #
from functools import partial
from datetime import date

AUTHOR = "Enda Farrell"
SITENAME = "endafarrell.net"
HOME_TOP_LEAD = "Engineering Lead."
CURRENTYEAR = date.today().year

# Unused, was for an older version of hte site, but a useful concept.
CATEGORY_DESC = {
    "dia": "relating to diabetes",
    "dev": "relating to code, development, technology",
    "ops": "relating to tech-ops, security, hardware, installations",
    "data": "relating to data, data science, visualisations",
}

# These two need to go together and be consistent! Note that as of 2019-07 articles are not used
ARTICLE_URL = "posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/index.html"

# Hide tags, archives, categories, authors
TAGS_SAVE_AS = None  # formerly "tags.html"
CATEGORIES_SAVE_AS = None  # formerly "categories.html"
ARCHIVES_SAVE_AS = None  # formerly "archives.html"
AUTHORS_SAVE_AS = None  # formerly "authors.html"

# As of 2019-07 the site is essentially "pages"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
SLUGIFY_SOURCE = "basename"

SUMMARY_MAX_LENGTH = 100  # words, unused

PATH = "content"

TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%a %Y-%m-%d"

# Feed generation is not used.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Adds jupyter notebooks to the file-types recognised as containing markup.
# @see https://github.com/danielfrg/pelican-ipynb
MARKUP = ("md", "ipynb")

# Adds the pelican-ipynb plugin - but as of 2019-07 it is not used
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["ipynb.markup", "pelican-page-hierarchy", "pelican-toc"]
IGNORE_FILES = [".ipynb_checkpoints"]

TOC = {"TOC_INCLUDE_TITLE": False}

STATIC_PATHS = ["images", "extra/CNAME", "extra/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}


def sidebar(value):
    if value.startswith("archives") or value.startswith("category"):
        return "right-sidebar"
    elif value == "index":
        return "index"
    else:
        return "no-sidebar"


JINJA_FILTERS = {
    "sort_by_article_count": partial(
        sorted, key=lambda tags: len(tags[1]), reverse=True
    ),  # reversed for descending order
    "sidebar": sidebar,
}
