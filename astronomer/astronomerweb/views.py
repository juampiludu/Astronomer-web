from django.shortcuts import render, redirect
from .models import Eclipses

# Create your views here.

def principal(request):
    sitename = 'Astromomer'
    return redirect('/my-weight', {'sitename' : sitename})

def weight(request):
    sitename = 'My Weight'
    return render(request, 'front/weight.html', {'sitename' : sitename})

def nextEclipses(request):
    sitename = 'Next Eclipses'
    solarEclipse = Eclipses.objects.filter(solar_lunar='Solar')
    lunarEclipse = Eclipses.objects.filter(solar_lunar='Lunar')
    return render(request, 'front/next_eclipses.html', {'sitename' : sitename, 'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse})

def about(request):
    sitename = 'About'
    return render(request, 'front/about.html', {'sitename' : sitename})

def mobileapp(request):
    solarEclipse = Eclipses.objects.filter(solar_lunar='Solar')
    lunarEclipse = Eclipses.objects.filter(solar_lunar='Lunar')
    return render(request, 'front/mobileapp.html', {'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse})