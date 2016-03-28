from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django import forms
from .forms import *
from locate.models import *
import json
import time

def user_login(request):
    login_form = LoginForm()
    context = {'login_form': login_form}
    next_page = request.GET['next']
    failed_login = False

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_staff and next_page == '/locate/dashboard/':
                        return redirect(next_page)
                    return redirect('/locate/')
            else:
                failed_login = True
                print('<<<<<<<< FAILED LOGIN >>>>>>>>>')
        else:
            print('Form is invalid')

    context['failed_login'] = failed_login
    return render(request, 'locate/login.html', context)

@login_required(login_url="/locate/login/")
def inclasshelp(request):
    layout = ClassroomLayout.objects.all()[0]
    # TODO: Add "active" property to classroom layouts and search using that property
    context = {'layout': layout}
    # TODO: Add queue to model
    # context['queue_count'] = 0
    question_form = StudentInputForm()
    fields = list(question_form)
    # context['question_form'] = question_form
    context['question_form'] = fields

    if request.method == 'POST':
        form = StudentInputForm(request.POST)
        if form.is_valid():
            ticket = Ticket()
            user = request.user
            ticket.student = Student.objects.get(user=user)
            ticket.student_question = form.cleaned_data['question']
            ticket.student_code = form.cleaned_data['code_submission']
            millis = int(round(time.time() * 1000))
            ticket.js_id = '{}-{}'.format(user.username, millis)
            ticket.save()
            location = StudentLocation()
            location.ticket = ticket
            location.xcoord = form.cleaned_data['xcoord']
            location.ycoord = form.cleaned_data['ycoord']
            location.img_width = form.cleaned_data['img_width']
            location.img_height = form.cleaned_data['img_height']
            location.save()
        else:
            print('FORM IS INVALID')

    return render(request, 'locate/classroom.html', context)

@login_required(login_url="/locate/login/")
def dashboard(request):

    locations = StudentLocation.objects.all()

    layout = ClassroomLayout.objects.all()[0]
    tickets = Ticket.objects.all()

    json_tickets = serializers.serialize('json', tickets)
    coordinates = serializers.serialize('json', locations)
    str_coords = json.loads(coordinates)

    counter = 0
    for coord in str_coords:
        coord['fields']['ticket'] = tickets[counter].js_id
        counter += 1

    coordinates = json.dumps(str_coords)

    context = {'layout': layout}
    context['tickets'] = tickets
    context['json_tickets'] = json_tickets
    context['coordinates'] = coordinates
    return render(request, 'locate/ta_dashboard.html', context)
