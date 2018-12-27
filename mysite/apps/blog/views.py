# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#from apps.webpage.models import Profile


def index(request):
    #user = Profile.objects.get(pk=1)
    return render(request, '404.html', {})
