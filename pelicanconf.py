#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Professor'
SITENAME = 'Cálculo Diferencial e Integral'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Campo_Grande'

DEFAULT_LANG = 'pt'

THEME = 'themes/verti'
THEME_STATIC_DIR = ''

ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_ORDER_BY = 'sortorder'
PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{category}/{slug}.html'

TAG_SAVE_AS = ''            # dir tags
TAGS_SAVE_AS = ''           # file tags.html
CATEGORY_SAVE_AS = ''       # dir categories
CATEGORIES_SAVE_AS = ''     # file categories.html
SUBCATEGORY_SAVE_AS = ''    # dir subcategories
SUBCATEGORIES_SAVE_AS = ''  # file subcategories.html
AUTHOR_SAVE_AS = ''         # dir authors
AUTHORS_SAVE_AS = ''        # file authors.html
ARCHIVES_SAVE_AS = ''       # file archives.html

PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors', 'subcategory']

STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Youtube', '#'),
         ('Curso da USP', '#'),)

# Social widget
SOCIAL = (('facebook', '#'),
          ('email', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
