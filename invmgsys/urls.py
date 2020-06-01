from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_system, name='inventory_system'),
]