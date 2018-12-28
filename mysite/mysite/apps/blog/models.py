# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True)
    labels = models.CharField(max_length=50)
    pud_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # TODO: add category and author

    def save(self, *args, **kwargs):
        if not self.id:
            slug = slugify(self.title)
        
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title