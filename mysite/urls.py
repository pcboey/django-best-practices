from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^grid/$', TemplateView.as_view(template_name='grid.html')),                   
    url(r'^books/', include('books.urls')),                   
    url(r'^admin/', include(admin.site.urls)),
)
