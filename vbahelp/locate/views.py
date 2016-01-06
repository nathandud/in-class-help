from django.shortcuts import render
from django.core import serializers
from django import forms
# from codemirror import CodeMirrorTextarea
from locate.models import *

def gethelp(request):
    layout = ClassroomLayout.objects.all()[0]
    # TODO: Add "active" property to classroom layouts and search using that property
    context = {'layout': layout}
    # TODO: Add queue to model
    context['queue_count'] = 0
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

    js_data = serializers.serialize('json', coord_data)

    context = {'layout': layout}
    context['js_data'] = js_data
    return render(request, 'locate/ta_dashboard.html', context)

class StudentInputForm(forms.Form):
    # codemirror_widget = CodeMirrorTextarea(mode="vbscript", theme="cobalt", config={ 'fixedGutter': True })
    # code_submission = forms.TextField(widget=codemirror_widget)
    question = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label='Question')
    code_submission = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False, label='Code')
    xcoord = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    ycoord = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    img_width = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    img_height = forms.DecimalField(widget=forms.HiddenInput(), required=True)

    def clean_question(self):
        data = self.cleaned_data['question']
        return data

    def clean_xcoord(self):
        data = self.cleaned_data['xcoord']
        return data

    def clean_ycoord(self):
        data = self.cleaned_data['ycoord']
        return data

    def clean_img_width(self):
        data = self.cleaned_data['img_width']
        return data

    def clean_img_height(self):
        data = self.cleaned_data['img_height']
        return data
