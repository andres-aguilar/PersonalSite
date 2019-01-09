# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)
    labels = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    content = MarkdownxField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']


    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)


    def __str__(self):
        return self.title