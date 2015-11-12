from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'authentication.views.index'),
    url(r'^login/', 'authentication.views._login'),
    url(r'^register/', 'authentication.views.register'),
    # url(r'^loginuser/', 'authentication.views._loginuser'),
    # url(r'^dashboard/', 'authentication.views.dashboard'),
    # url(r'^logout/', 'authentication.views._logout'),
    url(r'^getevent/', 'evm.views.getEvent'),
    url(r'^iamgoing/', 'evm.views.iamgoing'),
    url(r'^getmyevents/', 'evm.views.getMyEvents'),
)
