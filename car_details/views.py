from django.shortcuts import render
from car_models.models import Car, Image, Review, Booking

# Create your views here.


def car_details(request, id):

    context = {"data": Car.objects.get(id=id)}

    return render(request, 'car_details/car_details.html', context)
