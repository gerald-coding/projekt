from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=100)
    seats = models.IntegerField()
    transmission = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    rent_price = models.IntegerField()
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.car_model}"


class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image_url = models.ImageField(null=True, blank=True, upload_to="cars/images/")

    def __str__(self):
        return f"{self.car.brand} {self.car.car_model} - image {self.id}"


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=250, blank=True)
    score = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Booking(models.Model):

    car_customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    pickup_location = models.CharField(max_length=100, default='Tirane', null=True)
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    # price = models.IntegerField()
    status = models.CharField(max_length=20, default='pending', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.brand} {self.car.car_model} was booked by {self.car_customer} in {self.pickup_date} at {self.pickup_location}"
