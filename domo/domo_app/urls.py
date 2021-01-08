from django.urls import path
from django.conf.urls import url
from domo_app import views

# TEMPLATE TAGGING
app_name = 'domo_app'

urlpatterns = [
    path('test/',views.test, name='test'),
]