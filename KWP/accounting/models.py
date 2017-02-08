from django.db import models

# Create your models here.
class CostCode(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=200)
    vendorID = models.CharField(max_length=200)

    def __str__(self):
        if company:
            return self.company
        else:
            return self.name

class PurchaseOrder(models.Model):
    number = models.CharField(max_length=200)
    date = models.DateField()
    vendor = models.ForeignKey(Vendor)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    cost_code = models.ForeignKey(CostCode)

    def __str__(self):
        return self.number

class Expenses(models.Model):
    purchase_date = models.DateField()
    purchase_order = models.ForeignKey(PurchaseOrder)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    notes = models.TextField()
    ordered = models.BooleanField()
    delivered = models.BooleanField()
    
    
    
    
