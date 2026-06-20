from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True) #hem name, hem id, hem de email görünür olur
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username') #sadece username görünsün diye böyle yaptım
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'rating', 'description', 'active', 'created', 'update', 'product', 'user'] 
        #fields= "__all__"
        extra_kwargs= {
            'product': {'read_only':True, 'required': False}
        }
        #exclude = ['created'] bu alan çıkartılabilir bu şekilde. 
        #model Serializer kullandığımızda ekstra validasyon yazmamıza gerek yok, modelde ne varsa aynen geçerli olur. 

    def get_user(self, obj):
        return obj.user.username if obj.user else None