# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MyProjects, SocialMedia, Profile, Technologies, Schools, ProjectClasses, Work


admin.site.register(MyProjects)
admin.site.register(SocialMedia)
admin.site.register(Profile)
admin.site.register(Technologies)
admin.site.register(Schools)
admin.site.register(ProjectClasses)
admin.site.register(Work)