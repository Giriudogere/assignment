from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .forms import OrdersData
from import_export import resources
from django.forms import ValidationError
# Register your models here.
# class OrdersResource(resources.ModelResource):
#
#     class Meta:
#         model = orders
#
#         def before_import(self, dataset, using_transactions, dry_run, **kwargs):
#             for row in dataset:
#                 if decimal(row[3]) < 0:
#                     raise ValidationError('Sales shouls always be greater than 0 '
#                                       'Error in row with id = %s' % row[3])

@admin.register(orders)
class ordersAdmin(ImportExportModelAdmin):
    list_display = ('id','orderid','orderdate','orderquantity','sales','shipmode','profit','unitprice','customername','customersegment','productcategory')
#     form = OrdersData
#     Resource_class = OrdersResource
#
# admin.site.register(orders,ordersAdmin)
