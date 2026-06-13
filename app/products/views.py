from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.response import Response  

#default get requesti bunlar. 
@api_view(['GET', 'POST'])
def product_list(request):

    if request.method== 'GET':
        products= Product.objects.all()
        serializer = ProductSerializer(products, many=True) #products liste olarak geliyor
        return Response(serializer.data)
    if request.method=='POST':
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

   
@api_view()
def product_details(request, pk):
    product= Product.objects.get(pk=pk)
    serializer = ProductSerializer(product) #tekil bir bilgi alıyoruz
    return Response(serializer.data)


#SERILIZATION
""" DB'den örneğin bir veriyi aldık ve bunu kullanıcılara göndermeden önce bir serilization aracılığı ile json veriye dönüştürmemiz gerekiyor.
Django'da biz manuel halletmiş olsak da Django Rest Frameworku var. Serializer sınıfı var. Modellere dönüşüm yapacak olan serializer.py var. (BUrada validasyon kuralları da kullanılabiliyor.)
Kurulumu: pip install djangorestframework

def product_list(request):
    products = Product.objects.all()
    print(products) #queryset geri döndürecek 
    data={
        'products' : list(products.values())
    }
    return JsonResponse(data) #queryset direkt jsona çevrilmediği için yaptık.

def product_details(request, pk):
    product=get_object_or_404(Product, id=pk)
    data= {
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    }
    return JsonResponse(data)
    
    bu manuel yöntemdi.."""