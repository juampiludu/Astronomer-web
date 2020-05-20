from django.shortcuts import render, redirect

# Create your views here.

def principal(request):
    return redirect('/my-weight')

def weight(request):
    sitename = 'My Weight'
    return render(request, 'weight.html', {'sitename' : sitename})

def nextEclipses(request):
    sitename = 'Next Eclipses'
    return render(request, 'next_eclipses.html', {'sitename' : sitename})

def about(request):
    sitename = 'About'
    return render(request, 'about.html', {'sitename' : sitename})