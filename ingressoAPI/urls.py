from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from filmes import views


router = routers.DefaultRouter()
router.register('filmes/principal', views.FilmePrincipalViewSet, basename='FilmePrincipal')
router.register('filmes/alta', views.FilmeAltaViewSet, basename='FilmesAlta')
router.register('filmes/cartaz', views.FilmeCartazViewSet, basename='FilmesCartaz')
router.register('filmes', views.FilmeViewSet, basename='Filmes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
