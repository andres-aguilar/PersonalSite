from django.conf.urls import url

from .views import under_construction, index, error_404

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^$', under_construction, name='construction'),
    #url(r'^error/$', error_404, name='error'),
]

handler404 = error_404