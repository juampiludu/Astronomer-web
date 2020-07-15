from django.shortcuts import render, redirect
from .models import Eclipses
from adminpanel.models import Years
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your views here.

def mobileapp_safe_passage(request):
    return redirect('mobileapp', year=2020)

def weight(request):
    sitename = _('My Weight')
    #current_year = datetime.now().year
    return render(request, 'front/weight.html', {'sitename' : sitename})

def nextEclipses(request, year):
    try:
        years = Years.objects.all().order_by('year')
        display = Years.objects.get(year=year)
        sitename = _('Next Eclipses')
        solarEclipse = Eclipses.objects.filter(solar_lunar='Solar').order_by('eclipse_date')
        lunarEclipse = Eclipses.objects.filter(solar_lunar='Lunar').order_by('eclipse_date')
    except:
        sitename = '500 Server Error'
        return render(request, 'front/500.html', {'year' : year, 'sitename' : sitename, 'years' : years})
    return render(request, 'front/next_eclipses.html', {'sitename' : sitename, 'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse, 'years' : years, 'display' : display, 'year' : year})

def about(request):
    sitename = _('About')
    return render(request, 'front/about.html', {'sitename' : sitename})

def mobileapp(request, year):
    years = Years.objects.all().order_by('year')
    display = Years.objects.get(year=year)
    sitename = _('Next Eclipses')
    solarEclipse = Eclipses.objects.filter(solar_lunar='Solar').order_by('eclipse_date')
    lunarEclipse = Eclipses.objects.filter(solar_lunar='Lunar').order_by('eclipse_date')
    return render(request, 'front/mobileapp.html', {'sitename' : sitename, 'solarEclipse' : solarEclipse, 'lunarEclipse' : lunarEclipse, 'years' : years, 'display' : display, 'year' : year})