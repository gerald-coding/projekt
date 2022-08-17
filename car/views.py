from django.shortcuts import render
from car_models.models import Car, Image, Review, Booking
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def car(request):
    qs = Car.objects.all()

    search_brand = request.GET.get('search_brand')
    search_year = request.GET.get('search_year')
    search_seats = request.GET.get('search_seats')
    search_transmission = request.GET.get('search_transmission')
    search_rent_price = request.GET.get('search_rent_price')
    search_pickup = request.GET.get('search_pickup')
    search_return = request.GET.get('search_return')

    if search_brand != '' and search_brand is not None:
        qs = qs.filter(Q(brand__icontains=search_brand))
    if search_year != '' and search_year is not None:
        qs = qs.filter(Q(year=search_year))
    if search_seats != '' and search_seats is not None:
        qs = qs.filter(Q(seats=search_seats))
    if search_transmission != '' and search_transmission is not None:
        qs = qs.filter(Q(transmission__icontains=search_transmission))
    if search_rent_price != '' and search_rent_price is not None:
        qs = qs.filter(Q(rent_price=search_rent_price))

    p = Paginator(qs, 2)
    page = request.GET.get('page')
    c_list = p.get_page(page)

    # images = Image.objects.filter()

    context = {'qs': qs, 'c_list': c_list, 'search_brand': search_brand}

    return render(request, 'car/car.html', context)