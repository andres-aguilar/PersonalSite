from django.contrib import admin
from markdownx import urls as markdownx
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    # Login/logout views
    url(r'^login/$', login, {'template_name': 'dashboard/login.html'}, name='login'),
    url(r'^logout', logout_then_login, name='logout'),
    # Apps views
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdownx/', include(markdownx)),
    url(r'^dashboard/', include('mysite.apps.dashboard.urls', namespace='dashboard')),
    url(r'^blog/', include('mysite.apps.blog.urls', namespace='blog')),
    url(r'^', include('mysite.apps.webpage.urls', namespace='website')),
]
