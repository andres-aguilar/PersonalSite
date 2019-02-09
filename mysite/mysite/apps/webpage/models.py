# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User


class ProjectClasses(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Project classes'

    def __str__(self):
        return self.name


class MyProjects(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300)
    technologies = models.CharField(max_length=300)
    description = MarkdownxField()
    icon = models.CharField(max_length=25)
    image = models.ImageField(upload_to="static/projects")
    url = models.URLField(blank=True)
    date = models.DateField()
    slug = models.SlugField(default='', blank=True)
    project_type = models.ForeignKey(ProjectClasses, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(MyProjects, self).save(*args, **kwargs)
    
    @property
    def formatted_markdown(self):
        return markdownify(self.description)


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=50)
    short_bio = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    languages = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class Schools(models.Model):
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=50)
    carrer = models.CharField(max_length=50)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.degree


class Work(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name


class Technologies(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/techs")
    description = models.CharField(max_length=250)
    url = models.URLField()
    percentage = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name