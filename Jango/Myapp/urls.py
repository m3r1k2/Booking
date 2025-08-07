from django.urls import path
from .views import home, roomlist, booking, main, user_booking, room_detail

urlpatterns = [
    path('', main, name='main'),
    path('home/', home, name='home'),
    path('booking/', booking, name='booking'),
    path('rooms/', roomlist, name='roomlist'),
    path('my-bookings/', user_booking, name='user_booking'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),


]