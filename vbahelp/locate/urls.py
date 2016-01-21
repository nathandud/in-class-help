from django.conf.urls import patterns, url
from django.conf import settings
from locate import views

urlpatterns = patterns('',
    url(r'^$', views.inclasshelp, name='inclasshelp'),
    url(r'^gethelp/', views.inclasshelp, name='incalsshelp'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
)
