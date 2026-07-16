# Configuration file for the Sphinx documentation builder.

project = 'Cheap Car Insurance'
author = 'Cheap Car Insurance'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

language = 'en'

html_title = "Cheap Car Insurance 2026"

# Sitemap
html_baseurl = html_baseurl = "https://cheap-car-insurance-cheap-car-insurance.readthedocs-hosted.com/en/latest/"
sitemap_url_scheme = "{link}"
