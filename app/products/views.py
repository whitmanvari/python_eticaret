from django.shortcuts import render
from .models import Product
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    print(products) #queryset geri döndürecek 
    data={
        'products' : list(products.values())
    }
    return JsonResponse(data) #queryset direkt jsona çevrilmediği için yaptık.


