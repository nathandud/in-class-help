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
            #TODO: Get authorized user instead of ndudley
            ticket = Ticket()
            ticket.student = Student.objects.all()[0]
            ticket.student_question = form.cleaned_data['question']
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

def dashboard(request):

    locations = []
    for student_location in StudentLocation.objects.all():
        new_location = location(student_location)
        locations.append(new_location)

    layout = ClassroomLayout.objects.all()[0]
    tickets = Ticket.objects.all()

    coordinates = serializers.serialize('json', locations)

    context = {'layout': layout}
    # context['locations'] = locations
    context['tickets'] = tickets
    context['coordinates'] = coordinates
    return render(request, 'locate/ta_dashboard.html', context)

class location:
    def __init__(self, studentLocation):
        self.x_coord = studentLocation.xcoord
        self.y_coord = studentLocation.ycoord
        self.student_name = '{} {}'.format(studentLocation.ticket.student.user.first_name,
            studentLocation.ticket.student.user.last_name)
