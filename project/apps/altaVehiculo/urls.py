from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'altaVehiculo'

urlpatterns = [
    path("", TemplateView.as_view(template_name="altaVehiculo/index.html"), name="home"),
    path('nuevo_alta_vehiculo',views.AltaVehiculoCreate.as_view(), name='create'),
    path('list_alta_vehiculo/', views.AltaVehiculoList.as_view(), name='list'),
    path("tabla/", TemplateView.as_view(template_name="altaVehiculo/tabla.html"), name="tabla"),
]
