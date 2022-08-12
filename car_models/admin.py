from django.contrib import admin
from .models import Car, Image, Review, Booking

# Register your models here.

admin.site.register(Car)
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(Booking)
