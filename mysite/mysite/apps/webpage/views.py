# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic import DetailView
from .models import MyProjects, SocialMedia, Profile, Technologies, Schools, Work

def under_construction(request):
    return render(request, 'under_construction.html')


def error_404(request):
    user = Profile.objects.get(pk=1)
    return render(request, '404.html', {'user': user})


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


class Project(DetailView):
    model = MyProjects
    template_name = 'webpage/project.html'

    def get_context_data(self, **kwargs):
        context = super(Project, self).get_context_data(**kwargs)
        context["user"] = Profile.objects.get(pk=1)
        context["social_medias"] = SocialMedia.objects.all()
        return context

