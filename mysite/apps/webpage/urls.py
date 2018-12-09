from django.conf.urls import url

from .views import under_construction, index

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^$', under_construction, name='construction'),
]
