from django import forms
from .models import orders


class OrdersData(forms.ModelForm):
	# if forms.is_valid():
		class Meta:
			model = orders
			fields = ('orderid','orderquantity','sales','shipmode','profit','unitprice')

			def clean(self):
				super(OrdersData, self).clean()

				sales = self.cleaned_data.get('sales')

				if sales < 0 or sales is blank or sales is null:
					self._errors['sales'] = self.error_class(['Only numerical value are allowed and should be greater than 0'])

				return self.cleaned_data


			# def sales_validation(value):
			#     if value < 0 or value is blank or value is null:
			#         raise ValidationError(
			#             _('%(value)s : Only numerical value are allowed and should be greater than 0'),
			#             params={'value': value},
			#         )
			#
			# def qty_validation(value):
			#     if value < 0:
			#         raise ValidationError(
			#             _('%(value)s : value should be non zero, non negative'),
			#             params={'value': value},
			#         )
			#
			# def profit_validation(value):
			#     if value == 0:
			#         raise ValidationError(
			#             _('%(value)s : please enter a non zero value'),
			#             params={'value': value},
			#         )
			#
			#
			# def ship_validation(value):
			#     if value != str('Regular Air') and value != str('Delivery Truck') and value != str('Express Air'):
			#         raise ValidationError(
			#             _('%(value)s : value not in Regular Air / Delivery Truck /  Express Air. please enter one of these'),
			#             params={'value': value},
			#         )

	# else:
	# 	errMsg= None
    # 	errMsg = [(k, v[0]) for k, v in form.errors.items()]
	# return HttpReponse(form.errors.as_json(), status=400)
