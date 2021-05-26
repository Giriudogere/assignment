from import_export import resources
from .models import orders
from tablib import Dataset

class OrdersResource(resources.ModelResource):
    class Meta:
        model = orders
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        for col in dataset:
            if col[4] == '':
                raise ValidationError('This field black. '
                                  'Error in row with id = %s' % col[4])
