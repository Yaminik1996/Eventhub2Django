from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/admin/')
def homecontest(request):
	if not request.user.is_superuser:
		return render('contest/404.djt')
	else:
		return render('contest/index.djt')


@login_required(login_url='/admin/')
def contestcheck(request):
	#Check the contest details


def contestresult(request):
	#Check the contest results


