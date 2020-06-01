from django.shortcuts import render
from invmgsys.models import Product, Part, PartsInProduct

def inventory_system(request):
    return render(request, 'invmgsys/inventory_system.html', {})



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