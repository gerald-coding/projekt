from car_models.models import Car, Booking


def check_availability(car, pickup_date, return_date):
    result = Booking.objects.filter(pickup_date__range=(pickup_date, return_date), car_id=car.id) | Booking.objects.filter(return_date__range=(pickup_date, return_date),  car_id=car.id)
    return not result or len(result) < 1
