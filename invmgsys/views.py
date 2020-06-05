from django.shortcuts import render
from invmgsys.models import *  # '*' means all. Product, Part, PartsInProduct, StorageLocation, WorkOrder


def inventory_system(request):
    # parts = Part.objects.filter().order_by('id')
    # parts = Part.objects.filter().order_by('id')
    # print('debugging part id', parts)
    return render(request, 'invmgsys/inventory_system.html')


def display_parts(request):
    parts = Part.objects.all()
    context = {
        'parts': parts,
        'header': 'Parts',
    }
    return render(request, 'invmgsys/inventory_system.html', context)


def add_part(request):
    print('test')
#     return add_item(request, LaptopForm)

# parts = Part.objects.all()
# storage_location = StorageLocation.objects.filter

# Create your views here.
def list_bom(request, product_id=None):
    # this is one product with the specified ID
    product = Product.objects.filter(id=product_id).first()
    # this is a list of all partsinproduct where product_id is the product id
    bom = PartsInProduct.objects.filter(product_id=product.id).all()

    # context contains all the python objects you want to use in a page
    context = {
        "bom": bom,
    }
    # render a page where context contains bom
    return render(request, 'list_bom', context)
