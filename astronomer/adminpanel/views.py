from django.shortcuts import render, redirect, get_object_or_404
from astronomerweb.models import Eclipses
from .models import Years
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Time functions

def parseTime(time):

    in_time = datetime.strptime(time, '%I:%M %p')
    out_time = datetime.strftime(in_time, '%H:%M')
    return out_time

def parseDate(date):

    a = datetime.strptime(date, '%m/%d/%Y')
    b = datetime.strftime(a, '%B %-d, %Y')
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

        if solar_lunar == "" or eclipse_type == "" or eclipse_info == "" or eclipse_date == "" or eclipse_time == "":
            error = "You have to complete all fields"
            return render(request, 'back/error_page.html', {'error' : error})

        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                title = f'{parseDate(eclipse_date)} at {parseTime(eclipse_time)} GMT ({eclipse_type})'
                datetimex = f'{parseDateForCountdown(eclipse_date)} {parseTime(eclipse_time)}:00'
                a = Eclipses(eclipse_title=title, solar_lunar=solar_lunar, eclipse_type=eclipse_type, eclipse_info=eclipse_info, eclipse_image_name=filename, eclipse_image_url=url, eclipse_date=eclipse_date, eclipse_time=eclipse_time, eclipse_datetime=datetimex)
                a.save()
                return redirect('eclipseTable')

            else:

                fs.delete()
                error = "This file is not supported. Make sure if you are uploading an image file"
                return render(request, 'back/error_page.html', {'error' : error})

        except:

            error = "Choose an image to upload"
            return render(request, 'back/error_page.html', {'error' : error})

    return render(request, 'back/add_eclipse.html')

def edit_eclipse(request, id):

    if len(Eclipses.objects.filter(id=id)) == 0:
        return render(request, 'back/500.html', {'id' : id})

    if not request.user.is_authenticated:
        return redirect('mylogin')

    eclipses = Eclipses.objects.get(id=id)

    if request.method == 'POST':

        solar_lunar = request.POST.get('solar_lunar')
        eclipse_type = request.POST.get('eclipse_type')
        eclipse_info = request.POST.get('eclipse_info')
        eclipse_date = request.POST.get('eclipse_date')
        eclipse_time = request.POST.get('eclipse_time')

        if solar_lunar == "" or eclipse_type == "" or eclipse_info == "" or eclipse_date == "" or eclipse_time == "":
            error = "You have to complete all fields"
            return render(request, 'back/error_page.html', {'error' : error})

        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith("image"):

                title = f'{parseDate(eclipse_date)} at {parseTime(eclipse_time)} GMT ({eclipse_type})'
                datetimex = f'{parseDateForCountdown(eclipse_date)} {parseTime(eclipse_time)}:00'

                fss = FileSystemStorage()
                fss.delete(eclipses.eclipse_image_name)

                eclipses.eclipse_title = title
                eclipses.solar_lunar = solar_lunar
                eclipses.eclipse_type = eclipse_type
                eclipses.eclipse_info = eclipse_info
                eclipses.eclipse_image_name = filename
                eclipses.eclipse_image_url = url
                eclipses.eclipse_date = eclipse_date
                eclipses.eclipse_time = eclipse_time
                eclipses.eclipse_datetime = datetimex
                eclipses.save()
                return redirect('eclipseTable')

            else:

                fs.delete()
                error = "This file is not supported. Make sure if you are uploading an image file"
                return render(request, 'back/error_page.html', {'error' : error})

        except:

            title = f'{parseDate(eclipse_date)} at {parseTime(eclipse_time)} GMT ({eclipse_type})'
            datetimex = f'{parseDateForCountdown(eclipse_date)} {parseTime(eclipse_time)}:00'
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

    try:

        eclipses = Eclipses.objects.get(id=id)
        fs = FileSystemStorage()
        fs.delete(eclipses.eclipse_image_name)
        eclipses.delete()

    except:

        return render(request, 'back/500.html', {'id' : id})

    return redirect('eclipseTable')

def add_year(request):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    years = Years.objects.all().order_by('year')

    if request.method == 'POST':

        year = request.POST.get('year')

        if year == "":

            error = "Please, enter a year"
            return render(request, 'back/error_page.html', {'error' : error})
            
        if len(Years.objects.filter(year=year)) != 0:

            error = "This year is already taken"
            return render(request, 'back/error_page.html', {'error' : error})

        year = Years(year=str(year))
        year.save()
        return redirect('add_year')

    return render(request, 'back/add_year.html', {'range' : range(2000, 2101), 'years' : years})

def delete_year(request, year):

    if not request.user.is_authenticated:
        return redirect('mylogin')

    try:

        years = Years.objects.get(year=year)

        years.delete()

        return redirect('add_year')
    
    except:

        return render(request, 'back/500-year.html', {'year' : year})
