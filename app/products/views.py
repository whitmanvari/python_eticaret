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

def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    data= {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    }
    return JsonResponse(data)