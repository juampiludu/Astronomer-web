from django.contrib import admin
from django.urls import path, include
from astronomerweb import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/setlang', include('django.conf.urls.i18n')),
    path('astronomerAdmin/', admin.site.urls),
    path('X9VMTFaGCKp5WMp8HDL/', views.mobileapp_safe_passage),
    path('astronomer-admin-panel/', include('adminpanel.urls')),
]

urlpatterns += i18n_patterns (
    path('', include('astronomerweb.urls'))
)

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
