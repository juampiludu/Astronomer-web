from django.contrib import admin
from django.urls import path, include
from adminpanel import views

urlpatterns = [
    path('', views.eclipseTable, name="eclipseTable"),
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name='mylogout'),
    path('add-eclipse/', views.add_eclipse, name='add_eclipse'),
    path('add-year/', views.add_year, name='add_year'),
    path('edit-eclipse/eclipseId=<id>', views.edit_eclipse, name='edit_eclipse'),
    path('delete-item/eclipseId=<id>', views.delete_item, name='delete_item'),
    path('delete-year/year=<year>', views.delete_year, name='delete_year'),
]