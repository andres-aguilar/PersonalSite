from django.conf.urls import url

from .views import UnderConstruction, Index, Project, ProjectList, Error404

urlpatterns = [
    #url(r'^$', UnderConstruction.as_view(), name='construction'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^portafolio/$', ProjectList.as_view(), name='projects'),
    url(r'^portafolio/(?P<slug>[-\w]+)/$', Project.as_view(), name='project_details'),
    #url(r'^error/$', Error404.as_view(), name='error'),
]

handler404 = Error404