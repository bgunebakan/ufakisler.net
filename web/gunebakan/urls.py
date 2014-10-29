from django.conf.urls import patterns, url

from gunebakan import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
