from django.contrib import admin
from .models import *

admin.site.register(Part)
admin.site.register(StorageLocation)
admin.site.register(Product)
admin.site.register(PartsInProduct)
admin.site.register(WorkOrder)
