from django.contrib import admin
from markdownx import urls as markdownx
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdownx/', include(markdownx)),
    url(r'^blog/', include('mysite.apps.blog.urls', namespace='blog')),
    url(r'^', include('mysite.apps.webpage.urls', namespace='website')),
]
