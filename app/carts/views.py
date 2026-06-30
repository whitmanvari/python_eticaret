from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import CartSerializer, CartItemSerializer

from products.models import Product
from .models import Cart, CartItem


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cart, created= Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)

        #Eğer cart_item zaten varsa, quantity artırılacak. Yoksa yeni cart_item oluşturulacak.
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)
            
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)

#generic üzerinden alabiliriz
class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        #tuple döndürüyor. Eğer cart yoksa yeni cart oluşturacak. Eğer varsa onu döndürecek.
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
