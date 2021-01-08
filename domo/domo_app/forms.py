from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField(label= '',widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    contact_number = forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    
    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    contact_number.widget.attrs.update({'class': 'form-control'})
