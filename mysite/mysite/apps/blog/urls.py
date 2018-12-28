from django.conf.urls import url

from .views import Index, ArticleDetail

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetail.as_view(), name='view')
]