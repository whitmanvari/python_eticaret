from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True) #formdan okuyabildiklerimi güncelleyemeyeceğim
    name = serializers.CharField()
    price= serializers.DecimalField(max_digits=10,decimal_places=2)
    stock= serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

#veritabanından aldıklarımızı veri süzgecinden geçirmemizi sağlıyor. Jsona manuel çevirmememiz için bir serileştirme işlemi yapıyor arka planda. Valdiasyon kuralları da aynen geçerli models.py içerisindeki. 
