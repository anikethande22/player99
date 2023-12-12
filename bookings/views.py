from django.shortcuts import render, redirect
from .models import Bookings

# Create your views here.
def bookings(request):
    bookings = Bookings.objects.filter(isdelivered=False)
    return render(request,'bookings/bookings.html', {"bookings": bookings})

def history(request):
    bookings = Bookings.objects.filter(isdelivered=True)
    return render(request,'bookings/history.html', {"bookings": bookings})

def update_booking(request, id):
    bookings = Bookings.objects.get(id=id)
    bookings.isdelivered = True
    bookings.save()
    return redirect('book')


