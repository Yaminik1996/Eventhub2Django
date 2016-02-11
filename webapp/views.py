from django.shortcuts import render

# Create your views here.


def testpage(request):
	return render('webapp/site/index/djt',{})