from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True) #formdan okuyabildiklerimi güncelleyemeyeceğim
    name = serializers.CharField()
    price= serializers.DecimalField(max_digits=10,decimal_places=2)
    stock= serializers.IntegerField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.description= validated_data.get('description', instance.description)
        instance.price= validated_data.get('price', instance.price)
        instance.stock= validated_data.get('stock', instance.stock)
        instance.save()
        return instance
#veritabanından aldıklarımızı veri süzgecinden geçirmemizi sağlıyor. Jsona manuel çevirmememiz için bir serileştirme işlemi yapıyor arka planda. Valdiasyon kuralları da aynen geçerli models.py içerisindeki. 
