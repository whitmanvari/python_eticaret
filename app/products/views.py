from .models import Product
from rest_framework.decorators import api_view, permission_classes
from .serializers import ProductSerializer, ProductListSerializer, ProductDetailsSerializer
from rest_framework.response import Response
from rest_framework import status  
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_list_products(request):
    """Admin: List all products"""
    products= Product.objects.all()
    serializer = ProductListSerializer(products, many=True) #products liste olarak geliyor
    return Response(serializer.data) #200 ok
    
@api_view(['GET'])
def catalog_list_products(request):
    """Catalog: List all products"""
    products= Product.objects.filter(stock__gt =0) #greater than 0
    serializer = ProductListSerializer(products, many=True) 
    return Response(serializer.data) 

@api_view(['GET'])
def catalog_product_details(request, pk):

    try:
        product= Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response('Error: Product not found.', status=status.HTTP_404_NOT_FOUND) # 404 not found yani aradığın id yok diyebiliriz.

    serializer = ProductDetailsSerializer(product) 
    return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_product_details(request, pk):

    try:
        product= Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response('Error: Product not found.', status=status.HTTP_404_NOT_FOUND) 
    
    serializer = ProductDetailsSerializer(product) 
    return Response(serializer.data)

#admin_create_product
@api_view(['POST'])
def admin_create_product(request):
    serializer= ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) #Bir veri karşı tarafa yüklendi, post oldu 201.  
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #post hatası varsa status 400 bad request.
        

#default get requesti bunlar. 
@api_view(['GET', 'POST'])
def product_list(request):

    if request.method== 'GET':
        products= Product.objects.all()
        serializer = ProductSerializer(products, many=True) #products liste olarak geliyor
        return Response(serializer.data) #200 ok
    
    if request.method=='POST':
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Bir veri karşı tarafa yüklendi, post oldu 201.  
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #post hatası varsa status 400 bad request.

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def admin_edit_product(request, pk):

    product= Product.objects.get(pk=pk)
    serializer = ProductSerializer(product,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT'])
def product_details(request, pk):

    if request.method == 'GET':
        try:
            product= Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response('Error: Product not found.', status=status.HTTP_404_NOT_FOUND) # 404 not found yani aradığın id yok diyebiliriz.
     
        serializer = ProductSerializer(product) #tekil bir bilgi alıyoruz
        return Response(serializer.data)
    
    if request.method == 'PUT':
        product= Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #post hatası varsa status 400 bad request.

 
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def admin_delete_product(request, pk):

    try:
        product= Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'Error': 'Product not found.'}, status=404) # 404 not found yani aradığın id yok diyebiliriz.
    product.delete()
    return Response({'message': 'Product Deleted'}, status=status.HTTP_204_NO_CONTENT)


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

