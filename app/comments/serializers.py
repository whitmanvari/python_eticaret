from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'rating', 'description', 'active', 'created', 'update', 'product'] 
        #fields= "__all__"
        extra_kwargs= {
            'product': {'read_only':True}
        }
        #exclude = ['created'] bu alan çıkartılabilir bu şekilde. 
        #model Serializer kullandığımızda ekstra validasyon yazmamıza gerek yok, modelde ne varsa aynen geçerli olur. 