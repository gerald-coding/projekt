from django.shortcuts import render
from car_models.models import Car, Image, Review, Booking

# Create your views here.


def car_details(request):


    return render(request, 'car_details/car_details.html')
