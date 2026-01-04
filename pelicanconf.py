"""Pelican configuration for local development."""

AUTHOR = ""
SITENAME = "waind.org"
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"

TIMEZONE = "America/Los_Angeles"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = False

# Theme
THEME = "themes/minimal"

# URL structure
ARTICLE_URL = "notes/{slug}/"
ARTICLE_SAVE_AS = "notes/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Use directory structure for pages
PATH_METADATA = r"pages/(?P<slug>.*)\.md"

# Static paths
STATIC_PATHS = ["images"]

# Disable unused features
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Custom menu items
MENUITEMS = [
    ("now", "/now/"),
    ("notes", "/notes/"),
]
