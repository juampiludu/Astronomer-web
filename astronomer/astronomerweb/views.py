from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def principal(request):
    sitename = 'Astromomer'
    return redirect('/my-weight', {'sitename' : sitename})

def weight(request):
    sitename = 'My Weight'
    return render(request, 'weight.html', {'sitename' : sitename})

def nextEclipses(request):
    sitename = 'Next Eclipses'
    solarEclipse = SolarEclipse.objects.all()
    lunarEclipse = LunarEclipse.objects.all()
    return render(request, 'next_eclipses.html', {'sitename' : sitename, 'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse})

def about(request):
    sitename = 'About'
    return render(request, 'about.html', {'sitename' : sitename})