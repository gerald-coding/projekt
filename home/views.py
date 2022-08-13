from django.shortcuts import render
from django.http import HttpResponse
from car_models.models import Car, Image, Review,Booking, User

# Create your views here.


# Homepage view
def home(request):

    featured_cars = Car.objects.filter(featured=True)

    latest_cars = Car.objects.all().order_by('-created')[:3]

    catch_user = request.user

    context = {'featured': featured_cars, 'latest': latest_cars, 'user': catch_user }

    return render(request, 'home/homepage.html', context)


# About page view
def about(request):

    return render(request, 'home/about.html')


# Contact us page view
def contact(request):

    return render(request, 'home/contact.html')