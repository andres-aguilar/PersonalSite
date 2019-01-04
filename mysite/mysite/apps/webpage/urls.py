from django.conf.urls import url

from .views import under_construction, index, error_404, Project

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<slug>[-\w]+)/$', Project.as_view(), name='project'),
    #url(r'^$', under_construction, name='construction'),
    #url(r'^error/$', error_404, name='error'),
]

handler404 = error_404