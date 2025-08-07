from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Booking
from .forms import BookingForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'Myapp/index.html')
def main(request):
    return render(request, 'Myapp/main.html')



def roomlist(request):
    rooms = Room.objects.all()
    return render(request,'Myapp/roomlist.html', {'rooms': rooms})
@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']


            existing_bookings = Booking.objects.filter(
                room=room,
                date_from__lt=date_to,
                date_to__gt=date_from
            )

            if existing_bookings.exists():
                messages.error(request, 'Ця кімната вже зайнята на обраний період.')
            else:

                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()
                messages.success(request, 'Бронювання успішно створено!')
                return redirect('booking')
    else:
        form = BookingForm()

    return render(request, 'Myapp/booking.html', {'form': form})

@login_required
def user_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'Myapp/user_booking.html', {'bookings': bookings})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'Myapp/room_detail.html', {'room': room})

