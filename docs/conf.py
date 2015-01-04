# -*- coding: utf-8 -*-
import os
from slugify import slugify


project = u'OpenApiaryFormat Reference'
author = u'BeeInt'
year = "2014"
description = ''

version = '0.1'
release = '0.1'


################################################################################################

extensions = []
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_static_path = ['_static']
htmlhelp_basename = slugify(project)
copyright = u"This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/."

latex_elements = {
}
latex_documents = [
  ('index', '{0}.tex'.format(slugify(project)), project,
   author, 'manual'),
]
man_pages = [
    ('index', slugify(project), project,
     [author], 1)
]

texinfo_documents = [
  ('index', slugify(project), project,
   author, slugify(project), description,
   'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
