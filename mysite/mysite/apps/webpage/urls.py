from django.conf.urls import url

from .views import under_construction, index, error_404, Project, ProjectList

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^portafolio/$', ProjectList.as_view(), name='projects'),
    url(r'^portafolio/(?P<slug>[-\w]+)/$', Project.as_view(), name='project_details'),
    #url(r'^$', under_construction, name='construction'),
    #url(r'^error/$', error_404, name='error'),
]

handler404 = error_404