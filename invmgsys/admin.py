from django.contrib import admin
from .models import Part
from .models import StorageLocation
from .models import Product
from .models import PartsInProduct
from .models import WorkOrder

admin.site.register(Part)
admin.site.register(StorageLocation)
admin.site.register(Product)
admin.site.register(PartsInProduct)
admin.site.register(WorkOrder)
