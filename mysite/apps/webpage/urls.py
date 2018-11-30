from django.conf.urls import url

from .views import under_construction, index, projects, curriculum

urlpatterns = [
    url(r'^site/$', index, name='index'),
    url(r'^site/projects/$', projects, name='projects'),
    url(r'^site/cv/$', curriculum, name='cv'),
    url(r'^$', under_construction, name='construction'),
]
