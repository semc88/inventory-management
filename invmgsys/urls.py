from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_system, name='inventory_system'),
    path('bom/', views.list_bom, name='list_bom'),
    path('parts/', views.display_parts, name='display_parts'),
    path('', views.add_part, name='add_part'),
]

