from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ufakisler.urls', namespace="ufakisler")),
    url(r'^gunebakan/', include('gunebakan.urls', namespace="gunebakan")),
    url(r'^saglamdis/', include('saglamdis.urls', namespace="saglamdis")),
)
