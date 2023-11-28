from django.forms import ModelForm
from .models import Car, Account, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('owner', 'make', 'model', 'year', 'color', 'picture')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserProfileForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'picture', 'caption']