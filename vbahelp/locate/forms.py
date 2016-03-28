from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label='Net ID')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label='Password')

    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        return data

class StudentInputForm(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False, label='Question')
    code_submission = forms.CharField(widget=forms.HiddenInput, required=False)
    xcoord = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    ycoord = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    img_width = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    img_height = forms.DecimalField(widget=forms.HiddenInput(), required=True)

    #TODO: Actually do some  validation perhaps
    def clean_question(self):
        data = self.cleaned_data['question']
        return data

    def clean_code(self):
        data = self.cleaned_data['code_submission']
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
