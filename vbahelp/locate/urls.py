from django.conf.urls import patterns, url
from django.conf import settings
from locate import views

urlpatterns = patterns('',
    url(r'^$', views.gethelp, name='gethelp'),
    url(r'^gethelp/', views.gethelp, name='gethelp'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
)
