# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MyProjects, SocialMedia, Profile


admin.site.register(MyProjects)
admin.site.register(SocialMedia)
admin.site.register(Profile)
