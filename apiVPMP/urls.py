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
    url(r'^report/(?P<pk>[0-9]+)/$','api.views.report_detail'),
    url(r'^report/filter/status=(?P<status>[0-2]{1})/$','api.views.report_status_filter'),
    url(r'^report/filter/gender=(?P<gender>[0-1]{1})/$','api.views.report_gender_filter'),
   # url(r'^report/filter/missing_date=(?P<day>[0-9]{2})/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})/$', 'api.views.report_date_filter'),
    url(r'^user/report/(?P<pk>[0-9]+)/$', 'api.views.user_report_detail'),
    url(r'^report/(?P<status>[0-2]{1})/(?P<missing_date>[0-9]{10})/(?P<state>[0-9]{2})/(?P<city>[0-9]{3})/(?P<gender>[0-1]{1})/(?P<birth_date>[0-9]{10}/)$', 'api.views.report_filter_list'),
    url(r'^report/comment/(?P<pk>[0-9]+)/$', 'api.views.report_comment_detail'),
    url(r'^imageReport/$', 'api.views.imageReport_list'),
    url(r'^imageReport/(?P<pk>[0-9]+)/$', 'api.views.imageReport_detail'),
    url(r'^comment/$', 'api.views.comment_list'),
    url(r'^comment/(?P<pk>[0-9]+)/$', 'api.views.comment_detail'),
)
