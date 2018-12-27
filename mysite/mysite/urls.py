from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^', include('apps.webpage.urls', namespace='website')),
]
