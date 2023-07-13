from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from admin_app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('admin_app/', include('admin_app.urls')),
    path('staff_app/', include('staff_app.urls')),
    path('client/',include('client.urls')),
    path('CRM/', include('CRM.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

