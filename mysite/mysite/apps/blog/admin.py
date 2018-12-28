# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Article, Category

admin.site.register(Category)
admin.site.register(Article, MarkdownxModelAdmin)
