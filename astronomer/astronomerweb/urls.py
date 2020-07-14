from django.urls import path
from astronomerweb import views
from django.contrib import admin

urlpatterns = [
    #path('', views.principal),
    path('', views.weight),
    path('next-eclipses/selected-year=<year>', views.nextEclipses, name='nextEclipses'),
    path('about/', views.about),
    path('X9VMTFaGCKp5WMp8HDL/selected-year=<year>', views.mobileapp, name='mobileapp'),
]
