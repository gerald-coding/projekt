from django.urls import path
from . import views
# from car_models.views import BookingList
# from .views import BookingListView
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('', views.account, name="account"),
    # path('booking_list/', BookingListView, name="BookingListView"),
    path('profile/', views.view_profile,
         name= 'profile'),
    path('profile/edit_profile/', views.edit_profile,
         name='edit_profile'),
    path('register/', views.registerPage,
      name='register'),
    path('logout/', views.logoutPage,
         name='logout'),
    path('login/', views.loginPage,
      name='login'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"),
         name="password_reset_complete"),
    path('account/my_listings/', views.my_listings, name="my_listings"),
    path('account/my_listings/list_a_car/', views.create_car, name='create_car'),
    path('account/my_listings/update_car/<int:id>', views.update_car, name='update_car'),
    path('account/my_listings/delete_car/<int:id>', views.delete_car, name='delete_car'),

]
