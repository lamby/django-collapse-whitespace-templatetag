django-collapse-whitespace-templatetag
======================================

A simple whitespace-collapsing template tag for Django - useful for formatting
plain text emails or when whitespace actually matters.

Installation
------------

 * Install to PYTHONPATH, etc.

Then either:

 * Add ``collapse_whitespace_templatetag`` to ``settings.INSTALLED_APPS`` and
   then use::

     {% load collapse_whitespace_templatetag %}

   ... in your templates.

Or:

 * Add ``collapse_whitespace_templatetag.templatetags.collapse_whitespace`` to
   your ``BUILTINS`` entry in ``settings.TEMPLATES`` (Django 1.9)

Or:

 * Add to builtins (< Django 1.9) with in some ``models.py``::

     from django.template.base import add_to_builtins
     add_to_builtins('collapse_whitespace_templatetag.templatetags.collapse_whitespace'
