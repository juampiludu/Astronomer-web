from django.shortcuts import render, redirect

# Create your views here.

def principal(request):
    return redirect('/my-weight')

def weight(request):
    return render(request, 'weight.html')
