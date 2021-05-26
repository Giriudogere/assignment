from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def sales_validation(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s : value should be greater than 0'),
            params={'value': value},
        )

def qty_validation(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s : value should be non zero, non negative'),
            params={'value': value},
        )

def profit_validation(value):
    if value == 0:
        raise ValidationError(
            _('%(value)s : please enter a non zero value'),
            params={'value': value},
        )


def ship_validation(value):
    if value != str('Regular Air') and value != str('Delivery Truck') and value != str('Express Air'):
        raise ValidationError(
            _('%(value)s : value not in Regular Air / Delivery Truck /  Express Air. please enter one of these'),
            params={'value': value},
        )
