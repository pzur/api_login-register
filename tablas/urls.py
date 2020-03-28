from django.urls import path,include
from .import views
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register('cliente',views.ClienteList)
routers.register('mascota',views.MascotaList)
routers.register('paseador',views.PaseadorList)

urlpatterns = [
    path('',include(routers.urls)),
    path('registrar/',views.Registros.as_view()),
    path('login/',views.LoginView.as_view()),
]
