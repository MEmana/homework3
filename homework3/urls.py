from django.conf.urls import patterns, include, url
from django.contrib import admin

    # Examples:
    # url(r'^$', 'homework3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^admin/', include(admin.site.urls)),
)
