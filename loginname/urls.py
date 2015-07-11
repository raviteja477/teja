from django.conf.urls import patterns, url


from . import views


urlpatterns = patterns('',
    # Examples:
     url(r'^index$', views.login, name='home'),
     url(r'^login-check$', views.login_check, name='home1'),
    
     
    
)
