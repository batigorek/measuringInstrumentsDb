from django.shortcuts import render
from .models import Instruments, Calipers, Micrometers

# Create your views here.

def instruments_home(request):
    instruments = Instruments.objects.order_by('title')
    return render(request, 'instruments/instruments_home.html', {'instruments': instruments})

def calipers(request):
    calipers = Calipers.objects.order_by('inv_number')
    return render(request, 'instruments/table_layout.html', {'instruments': calipers})

def micrometers(request):
    micrometers = Micrometers.objects.order_by('inv_number')
    return render(request, 'instruments/table_layout.html', {'instruments': micrometers})