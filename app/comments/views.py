from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import mixins

class CommentListView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer

    #*args (Positional arguments / Konumsal argümanlar) ve kwargs (Keyword arguments / İsimli argümanlar), Python'da bir fonksiyona veya metoda esnek sayıda argüman gönderilmesini sağlayan yapılardır.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #çift yıldız dictionarye koy, tek yıldız tuple olarak al 

    