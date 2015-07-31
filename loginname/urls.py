from django.conf.urls import patterns, url


from . import views


urlpatterns = patterns('',
    # Examples:
     
     url(r'^index$', views.login, name='home'),
     url(r'^login-check$', views.login_check, name='home1'),
     url(r'^welcome' , views.enter, name='home2'),
     url(r'^ticket', views.book, name='home3'),
    
     
    
)
