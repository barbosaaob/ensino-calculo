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

PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors']

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
