from django.shortcuts import render, redirect
from .models import Eclipses
from adminpanel.models import Years
from datetime import datetime

# Create your views here.

def principal(request):
    sitename = 'Astromomer'
    return redirect('/my-weight', {'sitename' : sitename})

def weight(request):
    sitename = 'My Weight'
    #current_year = datetime.now().year
    return render(request, 'front/weight.html', {'sitename' : sitename})

def nextEclipses(request, year):
    years = Years.objects.all()
    display = Years.objects.get(year=year)
    sitename = 'Next Eclipses'
    solarEclipse = Eclipses.objects.filter(solar_lunar='Solar')
    lunarEclipse = Eclipses.objects.filter(solar_lunar='Lunar')
    return render(request, 'front/next_eclipses.html', {'sitename' : sitename, 'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse, 'years' : years, 'display' : display, 'year' : year})

def about(request):
    sitename = 'About'
    return render(request, 'front/about.html', {'sitename' : sitename})

def mobileapp(request, year):
    years = Years.objects.all()
    display = Years.objects.get(year=year)
    sitename = 'Next Eclipses'
    solarEclipse = Eclipses.objects.filter(solar_lunar='Solar')
    lunarEclipse = Eclipses.objects.filter(solar_lunar='Lunar')
    return render(request, 'front/mobileapp.html', {'sitename' : sitename, 'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse, 'years' : years, 'display' : display, 'year' : year})