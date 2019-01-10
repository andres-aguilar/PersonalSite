# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from mysite.apps.blog.models import Article
from mysite.apps.webpage.models import Profile, SocialMedia

from .forms import ArticleForm

@login_required(login_url='/login/')
def index(request):
    user = Profile.objects.get(pk=1)
    return render(request, 'dashboard/index.html', { 'user': user })


class CreatePost(LoginRequiredMixin, CreateView):
    login_url = 'login'
    template_name = 'dashboard/new_post.html'
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('dashboard:index')

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context["user"] = Profile.objects.get(pk=1)
        context["social_medias"] = SocialMedia.objects.all()
        return context