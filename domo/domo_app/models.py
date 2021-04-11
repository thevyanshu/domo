from django.db import models
import os
from twilio.rest import Client

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length= 255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)
    
    def __str__(self):
        return str(self.email)
    
    def __int__(self):
        return int(self.contact_number)
    
    def save(self, *args, **kwargs):
        account_sid = 'AC76d0fa3dc2142d50ce465a42464d386a'
        auth_token = 'a686af17522d586615a44adaff7e3bc6'
        client = Client(account_sid, auth_token)
        
        numbers = {
            'Div':'+917073205980',
            'Anu': '+917755890311'
        }
        
        for name, number in numbers.items():
            message = client.messages.create(
                to=number,
                from_='+15128172331',
                body=f"Name - {self.name}, Email - {self.email}, Contact - {self.contact_number}"
            )
            print (message.sid)

