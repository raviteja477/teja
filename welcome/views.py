from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json

# Create your views here.

def book(request):
	template = loader.get_template('loginname/book.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
