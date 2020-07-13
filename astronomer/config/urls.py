from django.contrib import admin
from django.urls import path, include
from astronomerweb import views

urlpatterns = [
    path('astronomerAdmin/', admin.site.urls),
    path('', views.principal),
    path('my-weight/', views.weight),
    path('next-eclipses/selected-year=<year>', views.nextEclipses, name='nextEclipses'),
    path('about/', views.about),
    path('X9VMTFaGCKp5WMp8HDL/selected-year=<year>', views.mobileapp, name='mobileapp'),
    path('astronomer-admin-panel/', include('adminpanel.urls')),
]
