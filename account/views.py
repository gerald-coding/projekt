from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
# from car_models.views import BookingList
from car_models.models import Car, Booking
from django.views.generic import ListView, FormView, View


# Create your views here.

#
# def account(request):
#
#     return render(request, 'account/account.html')


# def BookingListView(self, request):
#     booking_list=Booking.objects.filter(car_customer=self.request.user)
#     context = {
#         'booking_list': booking_list
#     }
#     return render(request, context)

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
    args = {'user': request.user}
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
