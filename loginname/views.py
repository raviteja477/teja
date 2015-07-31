from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
import json

# Create your views here.

def login(request):
	template = loader.get_template('loginname/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def enter(request):
	template = loader.get_template('loginname/enter.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
	

def book(request):
	template = loader.get_template('loginname/book.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
	
	

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']

	if (username == 'raviteja' and password == '12345'):
		
		return HttpResponse("login successful")
	else:
		return HttpResponse("login failed")  
	
 
