from django.db import models
from django.db.models import IntegerField


class Part(models.Model):
    # id = models.CharField(min_length=10, max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    creator = models.CharField(max_length=50)


class StorageLocation(models.Model):
    # id = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    part_id = models.ForeignKey(Part, unique=False, null=True, on_delete=models.SET_NULL, blank=True)  # zero to many
    qty = models.IntegerField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)


class PartsInProduct(models.Model):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    part_id = models.ForeignKey(Part, null=True, on_delete=models.SET_NULL)
    qty = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = (('product_id', 'part_id'),)


class WorkOrder(models.Model):
    # Work Order Number is primary value but created by Django
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    due_date = models.DateField()
    qty = models.IntegerField(max_length=None)

# class BOM(models.Model):
# id = models.CharField(max_length=10, primary_key=True)
# part_id =  models.ForeignKey(Part, on_delete=models.CASCADE)
# qty

# class Product(models.Model):
# SKU =

# class Product(models.Model):
# name = models.CharField(max_length=50)

# class ProductPart(models.Model):
# product = models.ForeignKey(Product, on_delete=models.CASCADE)
# part = models.ForeignKey(Part, on_delete=models.CASCADE)


# class Part(models.Model):
# id = models.CharField(min_length=10, max_length=10, primary_key=True)
# name = models.CharField(max_length=50)
# desc = models.CharField(max_length=200)
# creator = models.CharField(max_length=50)
# storage_location = models.ForeignKey(StorageLocation, null=True, on_delete=models.SET_NULL)


# class StorageLocation(models.Model):
# id = models.CharField(max_length=10, primary_key=True)
# part_id = models.ForeignKey(Part, null=True, on_delete=models.SET_NULL)
# part_id = models.ForeignKey(Part, null=True, on_delete=models.SET_NULL)
# part_id = models.OneToOneField(Part, null=True, on_delete=models.SET_NULL) #zero or one and only one (both wAyz)
# part_id = models.ForeignKey(Part, null=False, on_delete=models.SET_NULL) #One to many

# These 2 below
# part_id = models.ForeignKey(Part, null=True, on_delete=models.SET_NULL)  # zero to many
# description = models.CharField(max_length=255, null=True, blank=True)

# qty = models.IntegerField(max_length=None)
