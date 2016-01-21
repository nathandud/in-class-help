from django.shortcuts import render
from django.core import serializers
from django import forms
from .forms import StudentInputForm
from locate.models import *

def inclasshelp(request):
    layout = ClassroomLayout.objects.all()[0]
    # TODO: Add "active" property to classroom layouts and search using that property
    print('THIS HAS DEALT WITH THE RESPONSE')
    context = {'layout': layout}
    # TODO: Add queue to model
    # context['queue_count'] = 0
    question_form = StudentInputForm()
    fields = list(question_form)
    # context['question_form'] = question_form
    context['question_form'] = fields

    if request.method == "POST":
        form = StudentInputForm(request.POST)
        if form.is_valid():
            print('FORM IS VALID')
            location = StudentLocation()
            location.xcoord = form.cleaned_data['xcoord']
            location.ycoord = form.cleaned_data['ycoord']
            location.img_width = form.cleaned_data['img_width']
            location.img_height = form.cleaned_data['img_height']
            location.save()
        else:
            print('FORM IS INVALID')

    return render(request, 'locate/classroom.html', context)

def dashboard(request):
    coord_data = StudentLocation.objects.all()
    layout = ClassroomLayout.objects.all()[0]
    tickets = Ticket.objects.all()

    js_data = serializers.serialize('json', coord_data)

    context = {'layout': layout}
    context['tickets'] = tickets
    context['js_data'] = js_data
    return render(request, 'locate/ta_dashboard.html', context)
