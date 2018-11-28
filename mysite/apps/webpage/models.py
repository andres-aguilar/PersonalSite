from django.db import models

# Create your models here.
class MyProjects(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=25)
    url = models.URLField()

    def __str__(self):
        return self.name