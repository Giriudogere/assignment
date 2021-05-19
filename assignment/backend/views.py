# Create your views here.
from django.contrib.sessions.models import Session
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from .resources import OrdersResource
from tablib import Dataset
from .models import orders
from django.core.exceptions import ValidationError
from .forms import OrdersData
from django.http import JsonResponse
import os

def export(request):
    orders_resource = OrdersResource()
    dataset = OrdersResource().export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="orders.xls"'
    return response

def data_upload(request):
    # if OrdersData().is_valid():
        if request.method == 'POST':
            orders_resource = OrdersResource()
            dataset = Dataset()
            new_orders = request.FILES['myfile']
            if not new_orders.name.endswith('xlsx'):
                extensionerror = '<body style="background-color:powderblue;"><h2><i>Invalid file format, please select .xlsx files only </i></h2><b><a href>Home</a></b><br><br><b><a href=/export>Export data</a>'
                return HttpResponse(extensionerror)
            imported_data = dataset.load(new_orders.read(),format='xlsx')
            global count
            #print(imported_data)
            for data in imported_data:
                count = 1
                if data[3]  == None :
                        column = 'Ordered Quantity'
                        error = 'Value should not be Blank, Please provide proper value'
                        data = [
                                {
                                'Column':column,
                                'Data':data[3],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[3]  < 0:
                        column = 'Ordered Quantity'
                        error = 'Value should be greater than 0'
                        data = [
                                {
                                'Column':column,
                                'Data':data[3],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[4] == None :
                        column = 'Sales'
                        error = 'Value should not be Blank, Please provide proper value.'
                        data = [
                                {
                                'Column':column,
                                'Data':data[4],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[4] < 0:
                        column = 'Sales'
                        error = 'Value should be greater than 0'
                        data = [
                                {
                                'Column':column,
                                'Data':data[4],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[6] == None:
                    column = 'Profit'
                    error = 'Value should not be Blank, Please provide proper value'
                    data = [
                            {
                            'Column':column,
                            'Data':data[6],
                            # 'Cell':count,
                            'Error':error
                            }
                           ]
                    return JsonResponse(data,safe=False)
                elif data[6] == 0 :
                        column = 'Profit'
                        error = 'Value should not be 0.'
                        data = [
                                {
                                'Column':column,
                                'Data':data[6],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[5] == None:
                        column = 'Shipmode'
                        error = 'Value should not be Blank, Please provide proper value.'
                        data = [
                                {
                                'Column':column,
                                'Data':data[5],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[5] != str('Regular Air') and data[5] != str('Delivery Truck') and data[5] != str('Express Air'):
                        column = 'Shipmode'
                        error = 'Value should be in Regular Air | Delivery Truck | Express Air'
                        data = [
                                {
                                'Column':column,
                                'Data':data[5],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[7] == None:
                    column = 'Unit Price'
                    error = 'Value should not be Blank, Please provide proper value'
                    data = [
                            {
                            'Column':column,
                            'Data':data[7],
                            # 'Cell':count,
                            'Error':error
                            }
                           ]
                    return JsonResponse(data,safe=False)
                elif data[7] == 0 :
                        column = 'Unit Price'
                        error = 'Value should not be 0'
                        data = [
                                {
                                'Column':column,
                                'Data':data[7],
                                # 'Cell':count,
                                'Error':error
                                }
                               ]
                        return JsonResponse(data,safe=False)
                elif data[2] == None:
                    column = 'Order Id'
                    error = 'Value should not be Blank, Please provide proper value'
                    data = [
                            {
                            'Column':column,
                            'Data':data[7],
                            # 'Cell':count,
                            'Error':error
                            }
                           ]
                    return JsonResponse(data,safe=False)
                elif data[2] == validate_slug:
                    column = 'Order Id'
                    error = 'Value can contain only Numbers or underscore'
                    data = [
                            {
                            'Column':column,
                            'Data':data[7],
                            # 'Cell':count,
                            'Error':error
                            }
                           ]
                    return JsonResponse(data,safe=False)

                else:
                	print(data[1])
                	value = orders(
                		data[0],
                		data[1],
                		 data[2],
                		 data[3],
                		 data[4],
                 		 data[5],
                 		 data[6],
                 		 data[7],
                 		 data[8],
                		 data[9],
                		 data[10],
                		)
                count = dataset.height
                value.save()
                html='<body style="background-color:powderblue;"><h2><i>Successfully uploadad %s rows to backend db </i></h2><b><a href>Home</a></b><br><br><b><a href=/export>Export data</a>' %count
            return HttpResponse(html)

        return render(request, 'input.html')
