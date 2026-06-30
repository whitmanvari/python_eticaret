from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price','quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)  # user alanını string olarak göstermek için

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']

    #Model üzerindeki get_total_price fonksiyonunu çağırmak için SerializerMethodField kullanıyoruz. 
    #SerializerMethodField, model üzerinde tanımlı bir metodu çağırmak için kullanılıyor. 
    # Bu durumda, Cart modelindeki get_total_price metodunu çağırmak için kullanıyoruz.
    def get_total_price(self, obj):
        return obj.get_total_price()


