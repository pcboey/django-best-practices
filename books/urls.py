from django.conf.urls import patterns, url
from .views import PublisherList

urlpatterns = patterns('',
    url(r'^publishers/$', PublisherList.as_view()),
)
