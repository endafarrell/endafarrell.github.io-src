# -*- coding: utf-8 -*- #
from functools import partial

AUTHOR = "Enda Farrell"
SITENAME = "endafarrell.net"
SITEURL = ""

DISCLAIMER = "These are my own personal opinions and are not endorsed by, nor do " \
     + "they represent the opinions of any previous, current nor future employers."

CATEGORY_DESC = {
    "dia": "relating to diabetes",
    "dev": "relating to code, development, technology",
    "ops": "relating to tech-ops, security, hardware, installations",
    "data": "relating to data, data science, visualisations"
}

# These two need to go together and be consistent!
ARTICLE_URL = "posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}-{date:%m}-{date:%d}/{slug}/index.html"
TAGS_SAVE_AS = 'tags.html'
CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_SAVE_AS = 'archives.html'

SUMMARY_MAX_LENGTH = 100  # words

PATH = "content"

TIMEZONE = "Europe/Berlin"
DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%a %Y-%m-%d"

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

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Adds jupyter notebooks to the file-types recognised as containing markup.
# @see https://github.com/danielfrg/pelican-ipynb
MARKUP = ("md", "ipynb")

# Adds the pelican-ipynb plugin
PLUGIN_PATHS = ["./plugins"]  # , "./pelican-plugins"]
PLUGINS = ["ipynb.markup"]   # , "assets", "materialbox"]
IGNORE_FILES = [".ipynb_checkpoints"]

# DISABLE GOOGLE_ANALYTICS = "UA-101964846-1"

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
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
