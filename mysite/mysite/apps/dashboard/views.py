# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from mysite.apps.webpage.models import Profile

@login_required(login_url='/login/')
def index(request):
    user = Profile.objects.get(pk=1)
    return render(request, 'dashboard/index.html', { 'user': user })


class CreatePost(LoginRequiredMixin, CreateView):
    pass
