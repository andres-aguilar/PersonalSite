# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from mysite.apps.webpage.models import Profile, SocialMedia

from .models import Article


class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'blog/list_articles.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context["user"] = Profile.objects.get(pk=1)
        context["social_medias"] = SocialMedia.objects.all()
        return context


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/article_view.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context["user"] = Profile.objects.get(pk=1)
        context["social_medias"] = SocialMedia.objects.all()
        return context