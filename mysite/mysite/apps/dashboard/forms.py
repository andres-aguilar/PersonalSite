# -*- coding: utf-8 -*-

import datetime
from django import forms
from django.contrib.auth.models import User
from markdownx.widgets import MarkdownxWidget
from markdownx.fields import MarkdownxFormField
from mysite.apps.blog.models import Article, Category

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Título',
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    labels = forms.CharField(
        label = 'Etiquetas',
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    pub_date = forms.DateTimeField(
        label = "Fecha de publicación",
        required = True,
        initial = datetime.datetime.now,
        widget = forms.DateTimeInput(attrs={'class': 'form-control'})
    )
    content = MarkdownxFormField(
        label = "Contenido de la publicación",
        required = True,
        widget = MarkdownxWidget(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        label = 'Categoría',
        queryset = Category.objects.all(),
        initial = 0,
        widget = forms.Select(attrs={'class': 'form-control'})
    )
    author = forms.ModelChoiceField(
        label = 'Autor',
        queryset = User.objects.all(),
        initial = 0,
        widget = forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Article
        fields = ('title', 'labels', 'pub_date', 'category', 'content', 'author')

