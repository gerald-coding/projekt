from django.shortcuts import render

# Create your views here.


def car_details(request):

    return render(request, 'car_details/car_details.html')
