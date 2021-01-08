from django.shortcuts import render
from domo_app import forms
from domo_app.models import User

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
            users = User()
            users.name = form.cleaned_data['name']
            users.email = form.cleaned_data['email']
            users.contact_number = form.cleaned_data['contact_number']
            users.save()
        else:
            form = forms.FormName()
    return render(request, 'domo_app/test.html', {'form':form})

def contact_us(request):
    return render(request, 'domo_app/contact_us.html')
