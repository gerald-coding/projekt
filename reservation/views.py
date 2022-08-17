from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, View
from car_models.models import Car, Booking
from .forms import AvailabilityForm
from reservation.booking_functions.availability import check_availability

# Create your views here.

class ReserveView(View):
    def get(self, request, *args, **kwargs):
        car_id = self.kwargs.get('id', None)
        form = AvailabilityForm
        car_list = Car.objects.filter(id=car_id)
        if len(car_list) > 0:
            car = car_list[0]
            context = {
                'car': car,
                'car_id': car.id,
                'car_brand': car.brand,
                'car_model': car.car_model,
                'car_transmission': car.transmission,
                'car_seats':car.seats,
                'car_type':car.type,
                'car_fuel': car.fuel,
                'car_rent_price':car.rent_price,
                'form': form,
            }
            return render(request, 'availability_form.html', context)
        else:
            return HttpResponse('Searching wrong')

    @method_decorator(login_required(login_url='login'))
    def post(self, request, *args, **kwargs):
        car_id = self.kwargs.get('id', None)
        car = Car.objects.filter(id=car_id).first()
        if not car:
            return HttpResponse('Vehicle not found in database!.')

        form = AvailabilityForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Form is not valid!.')

        data = form.cleaned_data

        if data['pickup_date'] > data['return_date']:
            return HttpResponse('Pickup date can not be greater than return date!.')

        if data['pickup_date'].timestamp() < datetime.today().timestamp():
            return HttpResponse('Pickup date can not be in the past!.')

        if not check_availability(car, data['pickup_date'], data['return_date']):
            return HttpResponse('This vehicle is booked for selected dates!.')

        booking = Booking.objects.create(
            car_customer=self.request.user,
            car=car,
            pickup_location=data['location'],
            pickup_date=data['pickup_date'],
            return_date=data['return_date'],
        )
        booking.save()
        return HttpResponse(booking)


class BookingList(ListView):
    model = Booking
    def get_queryset(self):
        booking_list= Booking.objects.filter(car_customer=self.request.user)
        return booking_list

