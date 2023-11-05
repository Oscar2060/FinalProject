from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from final_app.models import Car
from .forms import CarForm

# Create your views here.
def homepage(request):

   # Render the HTML template index.html with the data in the context variable.
   homepage_cars = Car.objects.order_by('-id')[:3]
   return render( request, 'final_app/homepage.html', { 'homepage_cars':homepage_cars })

def createCar(request):

   form = CarForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('home_page')
   return render(request, 'final_app/car_form.html', {'form':form})

def editCar(request, pk):

   car = get_object_or_404(Car, pk=pk)
   form = CarForm(request.POST or None, instance = car)
   if form.is_valid():
      form.save()
      return redirect('car-detail', pk)
   return render(request, 'final_app/car_form.html', {'form':form})

def deleteCar(request, pk):

   car = get_object_or_404(Car, pk=pk)
   if request.method=='POST':
      car.delete()
      return redirect('home_page')
   return render(request, 'final_app/delete_car.html', {'car':car})

class CarListView(generic.ListView):
   model = Car
class CarDetailView(generic.DetailView):
   model = Car

