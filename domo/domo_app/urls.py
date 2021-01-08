from django.urls import path
from django.conf.urls import url
from domo_app import views

# TEMPLATE TAGGING
app_name = 'domo_app'

urlpatterns = [
    path('test/',views.test, name='test'),
    path('contact_us/',views.contact_us, name = 'contact_us'),
    path('ngo/',views.ngo, name = 'ngo'),
    path('services/',views.services, name = 'services'),
    path('index/',views.index, name = 'index')
]