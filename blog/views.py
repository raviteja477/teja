from django.shortcuts import render

# Create your views here.

from blog.models import posts
 
def home(request):
	content = {
	       'title' : 'My first Post',
		'author':'Giles',
		'date' : '18 spetember'
	}
	return render_to_response{'index.html', content}
