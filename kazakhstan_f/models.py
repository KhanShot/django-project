from statistics import mode
from xxlimited import Null
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_type = models.TextField("User type", default='client')
    city = models.TextField("City", null=True, blank=True)
    name = models.TextField("Name", null=True, blank=True)
    age = models.IntegerField("Age", null=True, blank=True)
    

class Tours(models.Model):
    name = models.CharField('Tour name', max_length=100)
    description = models.CharField('Description', max_length=210)
    price = models.IntegerField('Price cost', null=True, blank=True)
    date = models.CharField('Date', blank=True,max_length=12)
    image = models.ImageField("image for tour",upload_to='images', blank=True, null=True)


class FormFeedbacks(models.Model):
    name = models.CharField("name", max_length=210)
    email = models.EmailField("email")
    phone = models.CharField("phone",max_length=210)
    message = models.TextField("message")