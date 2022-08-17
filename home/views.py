from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from car_models.models import Car, Image, Review, Booking, User



# Create your views here.


# Homepage view
def home(request):

    # car_list = Car.objects.all()
    #
    # c_id = None
    # for car in car_list:
    #     c_id = car.id
    #
    # image = Image.objects.filter(car_id=c_id)
    # image = image[0]

    featured_cars = Car.objects.filter(featured=True)

    latest_cars = Car.objects.all().order_by('-created')[:3]

    catch_user = request.user

    context = {'featured': featured_cars, 'latest': latest_cars, 'user': catch_user}

    return render(request, 'home/homepage.html', context)


# About page view
def about(request):

    return render(request, 'home/about.html')


# Contact us page view
def contact(request):

    return render(request, 'home/contact.html')

def SendMail(request):
    if request.method == 'POST':
        email=request.POST['email']
        msg=request.POST['msg']
        subject='Welcome to Rotors'
        message=msg
        from_email=email
        recipent_list=[settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,recipent_list,fail_silently=True)

        return HttpResponse('your message has been send successfully.')