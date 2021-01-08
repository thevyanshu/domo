from django.shortcuts import render
from domo_app import forms

# Create your views here.

def index(request) :
    return render(request, 'domo_app/index.html')

def test(request) :
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("CONTACT NUMBER: " + form.cleaned_data['contact_number'])
    return render(request, 'domo_app/test.html', {'form':form})
