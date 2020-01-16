"""papyrus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from repositorio import views

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)
routers.register(r'trabalho', views.TrabalhoList)

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')), # jet URLS
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_URL) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
