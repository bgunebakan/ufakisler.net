from django.conf.urls import patterns, url

from ufakisler import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)$', views.post_detail, name='post_detail'),
    url(r'^contact/$', views.contact, name='contact'),
)
