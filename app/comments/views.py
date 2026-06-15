from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
#from rest_framework import mixins

#ListAPIView(mixins.ListModelMixin.GenericAPIView)---> list api view aslında mixins'in Listmodelmixin'inin generic api view'indne türemiştir. Mixin kullanmadan direkt yazılabiliyor.
class CommentListView(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer

    """#*args (Positional arguments / Konumsal argümanlar) ve kwargs (Keyword arguments / İsimli argümanlar), Python'da bir fonksiyona veya metoda esnek sayıda argüman gönderilmesini sağlayan yapılardır.
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #çift yıldız dictionarye koy, tek yıldız tuple olarak al """

class CommentListByProductView(generics.ListAPIView):
    serializer_class= CommentSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Comment.objects.filter(product_id=pk)
    
class CommentDetailsView(generics.RetrieveAPIView):
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer

"""ListAPIView---> veritabanındaki birden fazla objeyi listelemek için kullanılır. 
Yaptığı: Veritabanından queryset'i çeker ve bunu serializer ile dönüştürür ve bir liste formatında döndürür. 

RetrieveAPIView(tekil veri)---> veritabından tek bir objeyi getirmek için kullanılır. 
Yaptığı: URL'den gelen pk veya slug gibi ID'yi kullanır. veritabanında sadece o ID' ye ait olan tek bir kaydı bulur ve 
tek bir obje (dictionary) olarak döner.


ListAPIView= GenericAPIView + ListModelMixin (listeleme yeteneği ekler)
RetrieveAPIView=GenericAPIView + RetrieveModelMixin (tekil veri öekme yeteneği ekler)"""