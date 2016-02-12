from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from webapp import views

urlpatterns = patterns('',
	url(r'events/',views.viewevents),
	url(r'^$',views.loginpage),
)