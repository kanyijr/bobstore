from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models import Product, Buyer, order, orderitem
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/', 
        'POST api/addtocart'
    ]

    return Response(routes)



