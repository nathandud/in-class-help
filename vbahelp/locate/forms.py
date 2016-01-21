from django import forms

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
