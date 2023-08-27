from django.db import models

# Create your models here.
from django.db import models
from phone_field import PhoneField

class Contact(models.Model):
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=130)
    company = models.CharField(max_length=130, null=True)
    email = models.EmailField(blank=False)
    phone = PhoneField(blank=True)
    message = models.TextField(blank=False)