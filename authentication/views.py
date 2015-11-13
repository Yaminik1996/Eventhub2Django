from django.shortcuts import render
from authentication.forms import UserForm,UserProfileForm
from datetime import datetime
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def _login(request):
	if request.method=="POST":
		username=request.POST.get('email',False)
		email = request.POST['email']
		password = request.POST['password']
		mobile_id=request.POST['id']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				user.lastLoginDate=datetime.now()
				user.userprofile.mobile_id=mobile_id
				user.userprofile.loggedIn=True
				user.save()
				return JsonResponse({'success':1,'message':'Success'})
			else:
				return JsonResponse({'success':0,'message':'Inactive'}) 
		else:
			return JsonResponse({'success':0,'message':'Email/Password incorrect'})


@csrf_exempt
def _logout(request):
	if request.method == "POST":
		userid=request.POST['id']
		user = User.objects.get(id=userid)
		if user is not None:
			user.userprofile.loggedIn=False
			user.save()
			return JsonResponse({'success':1})
		else:
			return JsonResponse({'success':0, 'message': "Invalid userid"})
	return JsonResponse({'success': 0, 'message': 'Invalid method'})


@csrf_exempt
def register(request):	
	registered = False
	response={}
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		print profile_form
		if user_form.is_valid() and profile_form.is_valid():
			
			user = user_form.save(commit=False)
			user.set_password(user.password)
			user.is_active=True
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.lastLoginDate = datetime.now()
			profile.ipaddress=get_client_ip(request)
			profile.save()
			registered = True
			response['success']=1
		else:
			print user_form.errors, profile_form.errors
			response['success']=0
	return JsonResponse(response)

