#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andrej Lukic'
SITENAME = 'Python and Machine Learning blog'
#SITEURL = 'http://crunchymebumblebee.org'
THEME = 'pelican-simplegrey'
OUTPUT_PATH = 'docs/'
#SITETAGLINE='this is a tagline'

STATIC_PATHS = ['posts', 'static', 'extra']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'
DEFAULT_LANG = 'en'
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-130113606-1"

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}  # and this
}

# Blogroll
#LINKS = (('Kaggle', 'https://www.kaggle.com/learn/machine-learning-explainability'),
#         ('Python.org', 'http://python.org/'),
#         ('Pelican', 'https://blog.getpelican.com/category/news.html'))

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/andrej-lukic/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True