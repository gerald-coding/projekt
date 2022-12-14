from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from car_models.models import Car, Image, Review, Booking
from .forms import ReviewForm

# Create your views here.


def car_details(request, id):

    car = Car.objects.get(id=id)
    user = request.user
    images = Image.objects.filter(car=car)
    reviews = Review.objects.filter(car_id=car.id)

    context = {'model': car, 'reviews': reviews, 'images': images, 'user': user}

    return render(request, 'car_details/car_details.html', context)


@login_required(login_url='login')
def review(request, id):

    user = request.user
    car = Car.objects.get(id=id)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form = Review.objects.create(
                user=user,
                car=car,
                feedback=data['feedback'],
                score=data['score']
            )
            form.save()

        return redirect('car_details')

    context = {'form': form}

    return render(request, 'car_details/review_form.html', context)


@login_required(login_url='login')
def update_review(request, id):

    review = Review.objects.get(id=id)
    user = request.user
    form = ReviewForm(instance=review)

    if request.user != review.user:
        return HttpResponse('You are not allowed to update this car')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()

            return redirect('car')

    context = {'form': form, 'review': review}
    return render(request, 'car_details/review_form.html', context)


@login_required(login_url='login')
def delete_review(request, id):

    review = Review.objects.get(id=id)
    user = request.user

    if request.user != review.user:
        return HttpResponse('You are not allowed to delete this car')

    if request.method == 'POST':
        review.delete()
        return redirect('car')
    return render(request, 'car_details/review_form.html', {'obj': review})
# CRUD views for Car listings end here
