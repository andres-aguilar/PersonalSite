# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import MyProjects, SocialMedia, Profile, Technologies, Schools, Work

def under_construction(request):
    return render(request, 'under_construction.html')


def error_404(request):
    return render(request, '404.html')


def index(request):
    projects = MyProjects.objects.all().order_by('-date')[:6]
    social_medias = SocialMedia.objects.all()
    user = Profile.objects.get(pk=1)
    technologies = Technologies.objects.all().order_by('-percentage')
    schools = Schools.objects.all().order_by('-start')
    works = Work.objects.all().order_by('-start')

    context = {
        'projects': projects,
        'social_medias': social_medias,
        'user': user,
        'technologies': technologies,
        'schools': schools,
        'works': works
    }

    return render(request, 'webpage/index.html', context)


def projects(request):
    return render(request, 'webpage/projects.html')


def curriculum(request):
    return render(request, 'webpage/cv.html')