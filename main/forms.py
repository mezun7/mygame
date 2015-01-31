__author__ = 'shuhrat'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})