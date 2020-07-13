from django.contrib import admin
from django.urls import path, include
from astronomerweb import views

urlpatterns = [
    path('astronomerAdmin/', admin.site.urls),
    path('', views.principal),
    path('my-weight/', views.weight),
    path('next-eclipses/', views.nextEclipses),
    path('about/', views.about),
    path('X9VMTFaGCKp5WMp8HDL/', views.mobileapp),
    path('astronomer-admin-panel/', include('adminpanel.urls')),
]
