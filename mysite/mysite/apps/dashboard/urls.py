# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import index, CreatePost

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new_post/$', CreatePost.as_view(), name="new_post")
]