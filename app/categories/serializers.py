from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField()
    description = serializers.CharField()

    #post
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    #put
    def update(self, instance, validated_data):
        instance.name=self.validated_data.get('name', instance.name)
        instance.description=self.validated_data.get('description', instance.description)
        instance.save()
        return instance