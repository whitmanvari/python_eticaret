from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = ['id', 'rating', 'description', 'active', 'created', 'update', 'product'] yapılabilir ya da all denilebilir
        fields= "__all__"
        #exclude = ['created'] bu alan çıkartılabilir bu şekilde. 
        #model Serializer kullandığımızda ekstra validasyon yazmamıza gerek yok, modelde ne varsa aynen geçerli olur. 