from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apiVPMP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),	
    url(r'^user/$', 'api.views.user_list'),
    url(r'^user/(?P<pk>[0-9]+)/$', 'api.views.user_detail'),
    url(r'^report/$', 'api.views.report_list'),
    url(r'^report/(?P<pk>[0-9]+)/$', 'api.views.report_detail'),
    url(r'^imageReport/$', 'api.views.imageReport_list'),
    url(r'^imageReport/(?P<pk>[0-9]+)/$', 'api.views.imageReport_detail'),
    url(r'^comment/$', 'api.views.comment_list'),
    url(r'^comment/(?P<pk>[0-9]+)/$', 'api.views.comment_detail'),
)
