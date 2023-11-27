from django.contrib import admin
from .models import Car, Account, Post

# Register your models here.

admin.site.register(Car)
admin.site.register(Account)
admin.site.register(Post)