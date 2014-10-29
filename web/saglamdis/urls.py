from django.conf.urls import patterns, url

from saglamdis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
