from django.db import models
from backend.validators import sales_validation, qty_validation, profit_validation, ship_validation
from django.core.validators import *
import django.db.backends.sqlite3.base

# Create your models here.
class orders(models.Model):
    # ship_mode = (
    #     ('Regular Air','Regular Air'),
    #     ('Delivery Truck','Delivery Truck'),
    #     ('Express Air','Express Air'),
    # )
    orderid = models.SlugField(validators=[validate_slug])
    orderdate = models.DateField(null=True)
    orderquantity = models.IntegerField(validators=[qty_validation])
    sales = models.DecimalField(validators=[sales_validation],decimal_places=2,max_digits=8, default=None)
    shipmode = models.CharField(max_length=100, validators=[ship_validation])
    profit = models.DecimalField(validators=[profit_validation],decimal_places=2,max_digits=8)
    unitprice = models.DecimalField(validators=[profit_validation],decimal_places=2,max_digits=8)
    customername = models.CharField(max_length=100)
    customersegment = models.CharField(max_length=100)
    productcategory = models.CharField(max_length=100)
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
