from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):

    owner = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    # modifications = models.TextField(max_length=200)
    # performance = models.TextField(max_length=200)

    # optional image
    # picture = 

    def __str__(self):
        return self.make + ' ' + self.model
    
    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])