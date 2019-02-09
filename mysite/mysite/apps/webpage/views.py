# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic import DetailView, ListView, TemplateView
from .models import MyProjects, SocialMedia, Profile, Technologies, Schools, Work

class UnderConstruction(TemplateView):
    template_name = 'under_construction.html'


class Error404(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super(Error404, self).get_context_data(**kwargs)
        context['user'] = Profile.objects.get(pk=1)
        return context


class Index(TemplateView):
    template_name = 'webpage/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['projects'] = MyProjects.objects.all().order_by('-date')[:6]
        context['social_medias'] = SocialMedia.objects.all()
        context['user'] = Profile.objects.get(pk=1)
        context['technologies'] = Technologies.objects.all().order_by('-percentage')
        context['schools'] = Schools.objects.all().order_by('-start')
        context['works'] = Work.objects.all().order_by('-start')
        return context


class ProjectList(ListView):
    model = MyProjects
    context_object_name = "project_list"
    template_name = "webpage/project_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context["user"] = Profile.objects.get(pk=1)
        context["social_medias"] = SocialMedia.objects.all()
        return context


class Project(DetailView):
    model = MyProjects
    context_object_name = "project"
    template_name = 'webpage/project_details.html'

    def get_context_data(self, **kwargs):
        context = super(Project, self).get_context_data(**kwargs)
        context["user"] = Profile.objects.get(pk=1)
        context["social_medias"] = SocialMedia.objects.all()
        return context

