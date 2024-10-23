# bookings/views.py

from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookingForm(initial={'reservation_date': timezone.now().date()})
    
    return render(request, 'bookings/booking_form.html', {'form': form})

def bookings_json(request):
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
        if bookings.exists():
            data = [{'first_name': b.first_name, 'reservation_slot': b.reservation_slot} for b in bookings]
        else:
            data = {'message': 'No Booking'}
    else:
        data = {'message': 'No Date Provided'}
    
    return JsonResponse(data, safe=False)
