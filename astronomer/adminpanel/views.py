from django.shortcuts import render, redirect
from astronomerweb.models import Eclipses
from django.contrib.auth import login, logout, authenticate
from datetime import datetime

# Time functions

def parseTime(time):

    in_time = datetime.strptime(time, '%I:%M %p')
    out_time = datetime.strftime(in_time, '%H:%M')
    return out_time

def parseDate(date):

    a = datetime.strptime(date, '%m/%d/%Y')
    b = datetime.strftime(a, '%B %-d')
    return b

def parseDateForCountdown(date):

    a = datetime.strptime(date, '%m/%d/%Y')
    b = datetime.strftime(a, '%b %-d, %Y')
    return b

# django functions

def eclipseTable(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    eclipses = Eclipses.objects.all()

    return render(request, 'back/eclipse_table.html', {'eclipses' : eclipses})

def mylogin(request):

    if request.user.is_authenticated:
        return redirect('eclipseTable')

    if request.method == 'POST':

        uuser = request.POST.get('username')
        upass = request.POST.get('password')

        if uuser != "" and upass != "":

            user = authenticate(username=uuser, password=upass)

            if user != None:

                login(request, user)
                return redirect('eclipseTable')

    return render(request, 'back/login.html')

def mylogout(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    logout(request)

    return redirect('mylogin')

def add_eclipse(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    eclipses = Eclipses.objects.all()

    if request.method == 'POST':

        solar_lunar = request.POST.get('solar_lunar')
        eclipse_type = request.POST.get('eclipse_type')
        eclipse_info = request.POST.get('eclipse_info')
        eclipse_date = request.POST.get('eclipse_date')
        eclipse_time = request.POST.get('eclipse_time')

        if solar_lunar != "" and eclipse_type != "" and eclipse_info != "" and eclipse_date != "" and eclipse_time != "":

            title = f'{parseDate(eclipse_date)} at {parseTime(eclipse_time)} GMT ({eclipse_type})'
            datetimex = f'{parseDateForCountdown(eclipse_date)} {parseTime(eclipse_time)}:00'
            a = Eclipses(eclipse_title=title, solar_lunar=solar_lunar, eclipse_type=eclipse_type, eclipse_info=eclipse_info, eclipse_date=eclipse_date, eclipse_time=eclipse_time, eclipse_datetime=datetimex)
            a.save()
            return redirect('eclipseTable')

    return render(request, 'back/add_eclipse.html')

def edit_eclipse(request, id):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    eclipses = Eclipses.objects.get(id=id)

    if request.method == 'POST':

        solar_lunar = request.POST.get('solar_lunar')
        eclipse_type = request.POST.get('eclipse_type')
        eclipse_info = request.POST.get('eclipse_info')
        eclipse_date = request.POST.get('eclipse_date')
        eclipse_time = request.POST.get('eclipse_time')

        if solar_lunar != "" and eclipse_type != "" and eclipse_info != "" and eclipse_date != "" and eclipse_time != "":

            title = f'{parseDate(eclipse_date)} at {parseTime(eclipse_time)} GMT ({eclipse_type})'
            datetimex = f'{parseDateForCountdown(eclipse_date)}, {parseTime(eclipse_time)}:00'
            
            eclipses.eclipse_title = title
            eclipses.solar_lunar = solar_lunar
            eclipses.eclipse_type = eclipse_type
            eclipses.eclipse_info = eclipse_info
            eclipses.eclipse_date = eclipse_date
            eclipses.eclipse_time = eclipse_time
            eclipses.eclipse_datetime = datetimex
            eclipses.save()
            return redirect('eclipseTable')

    return render(request, 'back/edit_eclipse.html', {'eclipses' : eclipses, 'id' : id})

def delete_item(request, id):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    eclipses = Eclipses.objects.get(id=id)

    eclipses.delete()

    return redirect('eclipseTable')