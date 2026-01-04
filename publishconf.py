"""Pelican configuration for production builds."""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401, F403

SITEURL = "https://waind.org"
RELATIVE_URLS = False

# Enable feeds in production
FEED_ALL_ATOM = "feeds/all.atom.xml"

# Delete output directory before regenerating
DELETE_OUTPUT_DIRECTORY = True
