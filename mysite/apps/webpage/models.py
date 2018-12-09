# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class ProjectClasses(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MyProjects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=25)
    image = models.ImageField(upload_to="static/projects")
    url = models.URLField()
    date = models.DateField()
    project_type = models.ForeignKey(ProjectClasses, on_delete=models.CASCADE)


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

    def __str__(self):
        return self.name