from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here
    
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True)
    bio = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('account-profile', args=[str(self.id)])
    
    
class Car(models.Model):
    owner = models.ForeignKey(Account, null=True, on_delete=models.CASCADE, default=None)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    # modifications = models.TextField(max_length=200)
    # performance = models.TextField(max_length=200)

    # optional image
    # picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.make + ' ' + self.model
    
    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])
    
class Post(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    caption = models.TextField(max_length=200, default='')
    # likes = (use if have time if not then focus on other things)

    # use max's as a base and go from there