from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from final_app.models import Car, Account, Post
from .forms import CarForm, CreateUserForm, UserProfileForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def homepage(request):

   homepage_cars = Car.objects.order_by('-id')[:3]
   accounts = Account.objects.all()
   
   return render( request, 'final_app/homepage.html', { 'homepage_cars':homepage_cars, 'accounts':accounts })

@login_required(login_url='login')
def createCar(request):

   form = CarForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('home_page')
   return render(request, 'final_app/car_form.html', {'form':form})

@login_required(login_url='login')
def editCar(request, pk):

   car = get_object_or_404(Car, pk=pk)
   form = CarForm(request.POST or None, instance = car)
   if form.is_valid():
      form.save()
      return redirect('car-detail', pk)
   return render(request, 'final_app/car_form.html', {'form':form})

@login_required(login_url='login')
def deleteCar(request, pk):

   car = get_object_or_404(Car, pk=pk)
   if request.method=='POST':
      car.delete()
      return redirect('home_page')
   return render(request, 'final_app/delete_car.html', {'car':car})

def registerPage(request):

   form = CreateUserForm()
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         username = form.cleaned_data.get('username')
         group = Group.objects.get(name='Users')
         user.groups.add(group)

         messages.success(request, 'Account was successfully created for ' + username)
         return redirect('create_profile')
   context = {'form':form}
   return render(request, 'registration/register.html', context)

def createProfile(request):

   form = UserProfileForm()
   if request.method == 'POST':
      form = UserProfileForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home_page')
   return render(request, 'final_app/profile_form.html', {'form':form})

@login_required(login_url='login')
def editAccount(request, pk):

   account = get_object_or_404(Account, pk=pk)
   form = UserProfileForm(request.POST or None, instance = account)
   if form.is_valid():
      form.save()
      return redirect('account-profile', pk)
   return render(request, 'final_app/profile_form.html', {'form':form})

@login_required(login_url='login')
def deleteAccount(request, pk) :

   account = get_object_or_404(Account, pk=pk)
   if request.method=='POST':
      account.delete()
      return redirect('home_page')
   return render(request, 'final_app/delete_car.html', {'account':account})

class CarListView(generic.ListView):
   model = Car
class CarDetailView(LoginRequiredMixin, generic.DetailView):
   model = Car
class AccountDetailView(LoginRequiredMixin, generic.DetailView):
   model = Account

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['account_cars'] = Car.objects.filter(owner_id=self.kwargs['pk'])
      return context
   
class PostListView(generic.ListView):
   model = Post
class PostDetailView(LoginRequiredMixin, generic.DetailView):
   model = Post
