from django.shortcuts import render
from django.core import serializers
from evm.models import Event,Content,UserEvents,EventRatings,UserFollow,Club
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
import datetime
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.sites.models import get_current_site
from django.utils.encoding import smart_str
from django.conf import settings
from django.core.mail import send_mail
import os
from django.core.files import File
from shutil import make_archive
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
from authentication.views import get_client_ip
from authentication.models import UserProfile

# Create your views here.


def loginpage(request):
	return render(request,'webapp/site/login.djt',{})

def viewevents(request):
	response={}
	dt=datetime.datetime.now()
	end_date = dt + datetime.timedelta(days=30)
	events=Event.objects.filter(date_time__range = (dt,end_date)).order_by('date_time')
	response['upcoming']=events
	end_date = dt - datetime.timedelta(days=30)
	events=Event.objects.filter(date_time__range = (dt,end_date))
	response['previous']=events
	events=Event.objects.filter(date_time__year=dt.year).filter(date_time__month=dt.month).filter(date_time__day=dt.day).order_by('date_time')
	response['today']=events
	return render(request,'webapp/site/index.djt',response)