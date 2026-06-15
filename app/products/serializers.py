from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator
from categories.models import Category
from comments.serializers import CommentSerializer
import re

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    name = serializers.CharField(max_length=200, validators= [UniqueValidator(queryset=Product.objects.all())])
    slug = serializers.CharField(validators= [UniqueValidator(queryset=Product.objects.all())])
    class Meta:
        model = Product
        #fields = "__all__" commentsi kapsamaz, eklemek için manuel yazabiliriz
        fields=['id', 'name', 'description', 'price', 'stock', 'slug', 'category', 'comments']

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Product name must be at least 3 characters.")
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        if value > 1000000:
            raise serializers.ValidationError("Price seems unusually high.")
        return value
    
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock can not be negative.")
        return value
    
    def validate_slug(self, value):
        if not re.match(r'^[a-z0-9\-]+$', value):
            raise serializers.ValidationError("Slug must be lower case and only contains hyphens and alphanumeric characters.")
        return value
    
    def validate(self, data):
        return data

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.description= validated_data.get('description', instance.description)
        instance.price= validated_data.get('price', instance.price)
        instance.stock= validated_data.get('stock', instance.stock)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
#veritabanından aldıklarımızı veri süzgecinden geçirmemizi sağlıyor. Jsona manuel çevirmememiz için bir serileştirme işlemi yapıyor arka planda. Valdiasyon kuralları da aynen geçerli models.py içerisindeki. 
