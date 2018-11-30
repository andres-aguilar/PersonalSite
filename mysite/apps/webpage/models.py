# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User



class MyProjects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=25)
    url = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.degree


class Technologies(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/techs")

    def __str__(self):
        return self.name