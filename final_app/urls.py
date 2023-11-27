from django.urls import path, include
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.homepage, name= 'home_page'),
path('cars/', views.CarListView.as_view(), name= 'cars'),
path('car/<int:pk>', views.CarDetailView.as_view(), name= 'car-detail'),
path('create_car/', views.createCar, name= 'create_car'),
path('car/<int:pk>/edit_car', views.editCar, name= 'edit_car'),
path('car/<int:pk>/delete_car', views.deleteCar, name= 'delete_car'),
path('accounts/register/', views.registerPage, name= 'register_page'),
path('accounts/create_profile/', views.createProfile, name='create_profile'),
path('account_profile/<int:pk>', views.AccountDetailView.as_view(), name='account-profile'),
path('account_profile/<int:pk>/edit_profile', views.editAccount, name= 'edit_account'),
path('account_profile/<int:pk>/delete_profile', views.deleteAccount, name= 'delete_account'),
]
