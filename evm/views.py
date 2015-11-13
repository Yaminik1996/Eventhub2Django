from django.shortcuts import render
from django.core import serializers
from evm.models import Event,Content,UserEvents,EventRatings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,JsonResponse
import datetime
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.sites.models import get_current_site
# Create your views here.


def homepage(request):
	return render(request,'site/home.html',{})


@csrf_exempt
def get_list_upcoming(request):
	response={}
	if request.method == "POST":
		date=request.POST['date']
		dt=datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") 
		end_date = dt + datetime.timedelta(days=30)
		events=Event.objects.filter(date_time__range = (dt,end_date))
		responsef=[]
		for e in events:
			response={}
			response['id']=e.id
			response['name']=e.name
			response['date']=e.date_time
			response['venue']=e.venue
			responsef.append(response)
		return JsonResponse(dict(events=responsef))
	return JsonResponse({'success': 0})

@csrf_exempt
def get_list_previous(request):
	response={}
	if request.method == "POST":
		date=request.POST['date']
		dt=datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") 
		end_date = dt - datetime.timedelta(days=30)
		events=Event.objects.filter(date_time__range = (dt,end_date))
		responsef=[]
		for e in events:
			response={}
			response['id']=e.id
			response['name']=e.name
			response['date']=e.date_time
			response['venue']=e.venue
			responsef.append(response)
		return JsonResponse(dict(events=responsef))
	return JsonResponse({'success': 0})



@csrf_exempt
def get_list_date(request):
	response={}
	if request.method == "POST":
		date=request.POST['date']
		dt=datetime.datetime.strptime(date, "%Y-%m-%d") 
		events=Event.objects.filter(date_time__year=dt.year).filter(date_time__month=dt.month).filter(date_time__day=dt.day)
		responsef=[]
		for e in events:
			response={}
			response['id']=e.id
			response['name']=e.name
			response['date']=e.date_time
			response['venue']=e.venue
			responsef.append(response)
		return JsonResponse(dict(events=responsef))
	return JsonResponse({'success': 0})


@csrf_exempt
def getEvent(request):
	if request.method == "POST":
		eventid=request.POST['id']
		event=Event.objects.get(id=eventid)
		users=UserEvents.objects.filter(event=event)
		ratings=EventRatings.objects.filter(event=event)
		response={}
		response['id']=event.id
		response['name']=event.name
		response['date']=event.date_time
		response['club']=event.club
		response['contact_name_1']=event.contact_name_1
		response['contact_number_1']=event.contact_number_1
		response['contact_name_2']=event.contact_name_2
		response['contact_number_2']=event.contact_number_2
		response['venue']=event.venue
		response['user_count']=len(users)
		response['content']=event.content.description
		response['average_rating']=ratings.aggregate(Avg('rating'))['rating__avg']
		# try:
		# 	img=open(event.content.image.path,'rb')
		# 	data=img.read()
		# 	response['image']="%s" % data.encode('base64')
		# except IOError:
		# 	return event.content.image.url
		response['image'] = get_current_site(request).domain+event.content.image.url
		return JsonResponse(response)
	return JsonResponse({'success': 0})


@csrf_exempt
def getuserlist(request):
	if request.method == "POST":
		eventid=request.POST['id']
		event=Event.objects.get(id=eventid)
		users=UserEvents.objects.filter(event=event)
		response={}
		response['users']=[]
		for u in users:
			response['users'].append(u.user.username)
		return JsonResponse(dict(users=response['users']))
	return JsonResponse({'success':0})



@csrf_exempt
def iamgoing(request):
	if request.method == "POST":
		eventid=request.POST['event_id']
		email=request.POST['email']
		uevent=UserEvents()
		event=Event.objects.get(id=eventid)
		user=User.objects.get(username=email)
		uevent.event=event
		uevent.user=user
		uevent.save()
		return JsonResponse({'success': 1})	
	return JsonResponse({'success': 0})

@csrf_exempt
def getMyEvents(request):
	if request.method == "POST":
		userid=request.POST['user_id']
		print userid
		user=User.objects.get(id=userid)
		events=UserEvents.objects.filter(user=user)
		print events
		responsef=[]
		for e in events:
			response={}
			response['id']=e.event.id
			response['name']=e.event.name
			response['date']=e.event.date_time
			response['venue']=e.event.venue
			responsef.append(response)
		return JsonResponse(dict(events=responsef))
	return JsonResponse({'success': 0})

@csrf_exempt
def addfeedback(request):
	if request.method == "POST":
		event_id=request.POST['event_id']
		user_id=request.POST['user_id']
		rating=request.POST['rating']
		feedback=request.POST['feedback']
		event=Event.objects.get(id=event_id)
		user=User.objects.get(id=user_id)
		review=EventRatings()
		review.event=event
		review.user=user
		review.rating=rating
		review.feedback=feedback
		review.save()
		return JsonResponse({'sucess':1, 'message': 'Review recorded'})
	return JsonResponse({'sucess':0, 'message': 'Invalid'})



