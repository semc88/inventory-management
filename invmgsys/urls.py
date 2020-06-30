from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parts/', views.display_parts, name='display_parts'),
    path('products/', views.display_products, name='display_products'),
    path('workorders/', views.display_workorders, name='display_workorders'),
    path('storage/', views.display_location, name='display_location'),
    path('bom/<int:product_id>/', views.display_bom, name='display_bom'),

    path('add_part/', views.add_part, name='add_part'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_workorder/', views.add_workorder, name='add_workorder'),
    path('add_location/', views.add_location, name='add_location'),
    path('add_bom/<int:product_id>', views.add_bom, name='add_bom'),

    path('edit_part/<int:pk>/', views.edit_part, name='edit_part'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('edit_workorder/<int:pk>/', views.edit_workorder, name='edit_workorder'),
    path('edit_location/<int:pk>/', views.edit_location, name='edit_location'),

    path('delete_part/<int:pk>/', views.delete_part, name='delete_part'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('delete_workorder/<int:pk>/', views.delete_workorder, name='delete_workorder'),
    path('delete_location/<int:pk>/', views.delete_location, name='delete_location'),


]
