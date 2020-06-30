from django import forms
from .models import *


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('name', 'desc', 'creator')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'desc')

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('product_id', 'start_date','due_date','qty')

class StorageLocationForm(forms.ModelForm):
    class Meta:
        model = StorageLocation
        fields = ('description', 'part_id','qty')

class PartsInProductForm(forms.ModelForm):
    class Meta:
        model = PartsInProduct
        fields = ('product_id', 'part_id','qty')


