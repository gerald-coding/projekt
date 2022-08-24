from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm, EditProfileForm, CarForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
# from car_models.views import BookingList
from car_models.models import Car, Booking, Image
from django.views.generic import ListView, FormView, View


def registerPage(request):
    if request.method == 'GET':
        return render(request, 'account/register.html',
                      {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'], email=request.POST['email'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('login')
            except IntegrityError:
                return render(request,
                              'account/register.html',
                              {'form': UserCreateForm,
                               'error': 'Username already taken. Choose new username.'})
        else:
            return render(request, 'account/register.html',
                          {'form': UserCreateForm,
                           'error': 'Passwords do not match'})


def logoutPage(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.method == 'GET':
        return render(request, 'account/login.html',
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'account/login.html',
                          {'form': AuthenticationForm(),
                           'error': 'username and password do not match'})
        else:
            login(request, user)
            return redirect('home')


def view_profile(request):

    booking_history = Booking.objects.filter(car__owner_id=request.user)

    args = {'user': request.user, 'booking_history': booking_history}

    return render(request, 'account/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)


# CRUD for Car listings start here
@login_required(login_url='login')
def create_car(request):

    user = request.user
    form_0 = CarForm()
    img_one = request.FILES.get('image_url_one')
    img_two = request.FILES.get('image_url_two')
    img_three = request.FILES.get('image_url_three')

    if request.method == 'POST':

        form_0 = CarForm(request.POST)

        if form_0.is_valid() and img_one != '' and img_one is not None and img_two != '' and img_two is not None and img_three != '' and img_three is not None:

            data_0 = form_0.cleaned_data

            car = Car.objects.create(
                owner=user,
                brand=data_0['brand'],
                car_model=data_0['car_model'],
                type=data_0['type'],
                year=data_0['year'],
                engine=data_0['engine'],
                seats=data_0['seats'],
                transmission=data_0['transmission'],
                fuel=data_0['fuel'],
                rent_price=data_0['rent_price'],
            )
            car.save()

            img_one = Image.objects.create(
                car=car,
                image_url=img_one,
            )
            img_one.save()

            img_two = Image.objects.create(
                car=car,
                image_url=img_two,
            )
            img_two.save()

            img_three = Image.objects.create(
                car=car,
                image_url=img_three,
            )
            img_three.save()

            return redirect('my_listings')

    context = {'form_0': form_0, 'img_one': img_one, 'img_two': img_two, 'img_three': img_three}

    return render(request, 'account/car_form.html', context)


@login_required(login_url='login')
def update_car(request, id):

    car = Car.objects.get(id=id)
    imgs = Image.objects.filter(car_id=car.id)
    img_1 = imgs[0].id
    img_2 = imgs[1].id
    img_3 = imgs[2].id

    form_0 = CarForm(instance=car)
    img_one = request.FILES.get('image_url_one')
    img_two = request.FILES.get('image_url_two')
    img_three = request.FILES.get('image_url_three')

    if request.user != car.owner:
        return HttpResponse('You are not allowed to update this car')

    if request.method == 'POST':
        form_0 = CarForm(request.POST, instance=car)
        if form_0.is_valid():
            form_0.save()

        a = Image.objects.get(id=img_1)
        if img_one != '' and img_one is not None:
            a.image_url = img_one
            a.save()

        b = Image.objects.get(id=img_2)
        if img_two != '' and img_two is not None:
            b.image_url = img_two
            b.save()

        c = Image.objects.get(id=img_3)
        if img_one != '' and img_one is not None:
            c.image_url = img_three
            c.save()

        return redirect('profile')

    context = {'form_0': form_0}
    return render(request, 'account/car_form.html', context)


@login_required(login_url='login')
def delete_car(request, id):

    car = Car.objects.get(id=id)

    if request.user != car.owner:
        return HttpResponse('You are not allowed to delete this car')

    if request.method == 'POST':
        car.delete()
        return redirect('profile')
    return render(request, 'account/delete_car_form.html', {'obj': car})
# CRUD views for Car listings end here


def my_listings(request):

    cars = Car.objects.filter(owner=request.user)

    context = {'cars': cars}
    return render(request, 'account/my_listings.html', context)
