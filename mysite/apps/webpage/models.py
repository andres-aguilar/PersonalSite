from django.db import models

# Create your models here.
class MyProjects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=25)
    url = models.URLField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name