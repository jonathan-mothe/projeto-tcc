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