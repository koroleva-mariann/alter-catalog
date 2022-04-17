import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.utils import timezone
from django.shortcuts import render
from .models import PriceLog, Product

# index
def index(request):
    return render(request, 'catalog/index.html')


# list of products
def product_list(request):
    product_list = []

    for p in Product.objects.all():
        product_list.append(model_to_dict(p))

    response = {
        'success' : True,
        'products' : product_list
        }

    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')


# update a product
def product_update(request):
    json_data = ''
    response = {
        'success' : False,
        'message' : 'Something went wrong'
        }

    try:
        json_data = json.loads(request.body.decode("utf-8"))
    except:
        response = {
            'success' : False,
            'message' : 'Wrong request format: JSON is expected'
            }
    else:
        if ('product_id' in json_data) and ('price' in json_data):
            product_id = json_data['product_id']
            price = json_data['price']

            if type(product_id) == int and type(price) == float or int:
                if price > 0:
                    product = Product.objects.get_by_id_or_null(product_id)
                    if product is not None:
                        product.uppdate_price(price)
                        response = {
                            'success' : True,
                            'message' : 'The product with id %s has been successfully updated' % product.id
                            }
                    else:
                        response = {
                            'success' : False,
                            'message' : 'The product with id %s was not found' % product_id
                            }
                else:
                    response = {
                        'success' : False,
                        'message' : 'The price should be more than 0'
                        }
            else:
                response = {
                    'success' : False,
                    'message' : 'The data specified has wrong format'
                    }
        else:
            response = {
                'success' : False,
                'message' : 'The response should contain the product id and price'
                }
    finally:
        return HttpResponse(json.dumps(response), content_type='application/json')

# list of prices
def pricelog_list(request):
    json_data = ''
    response = {
        'success' : False,
        'message' : 'Something went wrong'
        }

    try:
        json_data = json.loads(request.body.decode("utf-8"))
    except:
        response = {
            'success' : False,
            'message' : 'Wrong request format: JSON is expected'
            }
    else:
        if 'product_id' in json_data:
            product_id = json_data['product_id']
            
            if type(product_id) == int:
                pricelog_list = []

                for pl in PriceLog.objects.get_by_product_id(product_id):
                    pricelog_list.append({
                        'price' : pl.price,
                        'date' : pl.updated_date.strftime("%m/%d/%Y, %H:%M:%S")
                        })

                response = {
                    'success' : True,
                    'pricelog' : pricelog_list
                    }
            else:
                response = {
                    'success' : False,
                    'message' : 'The data specified has wrong format'
                    }
        else:            
            response = {
                'success' : False,
                'message' : 'The response should contain the product id'
                }
    finally:
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')