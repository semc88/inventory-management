from django.shortcuts import render, redirect, get_object_or_404
from invmgsys.models import *  # '*' means all. Product, Part, PartsInProduct, StorageLocation, WorkOrder
from invmgsys.forms import *
from django.shortcuts import render
from django.forms import inlineformset_factory

def index(request):
    # parts = Part.objects.filter().order_by('id')
    # parts = Part.objects.filter().order_by('id')
    # print('debugging part id', parts)
    return render(request, 'invmgsys/index.html')


def display_parts(request):
    parts = Part.objects.all()
    context = {
        'parts': parts,
        'header': 'Parts',
    }
    return render(request, 'invmgsys/parts.html', context)


def display_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'header': 'Products',
    }
    return render(request, 'invmgsys/products.html', context)


def display_workorders(request):
    workorders = WorkOrder.objects.all()
    context = {
        'workorders': workorders,
        'header': 'Work Orders',
    }
    return render(request, 'invmgsys/work_orders.html', context)

def display_location(request):
    locations = StorageLocation.objects.all()
    context = {
        'locations': locations,
        'header': 'Locations',
    }
    return render(request, 'invmgsys/storage.html', context)


def display_bom(request, product_id=None):
    # this is one product with the specified ID
    product = get_object_or_404(Product, id=product_id)

    # context contains all the python objects you want to use in a page
    context = {
        "product": product,
    }
    # render a page where context contains bom
    return render(request, 'invmgsys/bom.html', context)

#----------------------------------------ADD ACTION---------------------------------------------



def add_part(request):
    if request.method == "POST":
        form = PartForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_parts')
    else:
        form = PartForm()
        return render(request, 'invmgsys/add_item.html', {'form': form})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_products')
    else:
        form = ProductForm()
        return render(request, 'invmgsys/add_item.html', {'form': form})

def add_workorder(request):
    if request.method == "POST":
        form = WorkOrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_workorders')
    else:
        form = WorkOrderForm()
        return render(request, 'invmgsys/add_item.html', {'form': form})

def add_location(request):
    if request.method == "POST":
        form = StorageLocationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_location')
    else:
        form = StorageLocationForm()
        return render(request, 'invmgsys/add_item.html', {'form': form})


def add_bom(request, product_id):

    PartsInProductFormSet = inlineformset_factory(Product, PartsInProduct, fields=('product_id','part_id','qty'))
    product = get_object_or_404(Product, id=product_id)
    formset = PartsInProductFormSet(instance=product)

    if request.method == "POST":
        formset = PartsInProductFormSet(request.POST, instance= product)

        if formset.is_valid():
            formset.save()
            return redirect('display_products')

    context = {'form':formset}
    return render(request, 'invmgsys/add_edit_bom.html', context)

#--------------------------------------------EDIT-------------------------------------------------------

def edit_part(request, pk):  # cls is like the form?
    item = get_object_or_404(Part, pk=pk)

    if request.method == "POST":
        form = PartForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_parts')

    else:
        form = PartForm(instance=item)

        return render(request, 'invmgsys/edit_item.html', {'form': form})


def edit_product(request, pk):  # cls is like the form?
    item = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_products')

    else:
        form = ProductForm(instance=item)

        return render(request, 'invmgsys/edit_item.html', {'form': form})

def edit_workorder(request, pk):  # cls is like the form?
    item = get_object_or_404(WorkOrder, pk=pk)

    if request.method == "POST":
        form = WorkOrderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_workorders')
        return render(request, 'invmgsys/edit_item.html', {'form': form})
    else:
        form = WorkOrderForm(instance=item)

        return render(request, 'invmgsys/edit_item.html', {'form': form})

def edit_location(request, pk):  # cls is like the form?
    item = get_object_or_404(StorageLocation, pk=pk)

    if request.method == "POST":
        form = StorageLocationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_location')
        return render(request, 'invmgsys/edit_item.html', {'form': form})
    else:
        form = StorageLocationForm(instance=item)

        return render(request, 'invmgsys/edit_item.html', {'form': form})

#-----------------------------------------DELETE----------------------------------------------------------

def delete_part(request, pk):
    Part.objects.filter(id=pk).delete()

    items = Part.objects.all()

    context = {
        'items': items
    }

    return render(request, 'invmgsys/index.html', context)


def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()

    items = Product.objects.all()

    context = {
        'items': items
    }

    return render(request, 'invmgsys/index.html', context)


def delete_workorder(request, pk):
    WorkOrder.objects.filter(id=pk).delete()

    items = WorkOrder.objects.all()

    context = {
        'items': items
    }

    return render(request, 'invmgsys/index.html', context)


def delete_location(request, pk):
    StorageLocation.objects.filter(id=pk).delete()

    items = StorageLocation.objects.all()

    context = {
        'items': items
    }

    return render(request, 'invmgsys/index.html', context)



#----------------------------EXTRA STUFF--------------------------------------

def list_bom2(request, product_id=None):
    # this is one product with the specified ID
    product = Product.objects.filter(id=product_id).first()
    # this is a list of all partsinproduct where product_id is the product id
    bom = PartsInProduct.objects.filter(product_id=product.id).all()

    # context contains all the python objects you want to use in a page
    context = {
        "bom": bom,
    }
    # render a page where context contains bom
    return render(request, 'list_bom2', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'invmgsys/add_item.html', {'form': form})


def add_part2(request, cls):
    return add_item(request, cls)


def edit_item(request, pk, model, cls):  # cls is like the form?
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)

        return render(request, 'invmgsys/edit_item.html', {'form': form})


def edit_part2(request, pk):
    return edit_item(request, pk, Part, PartForm)
