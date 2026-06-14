from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=200) #karakter tabanlı bir veri alanı yansıyacak veritabanına.
    description= models.TextField(blank=True, null=True) #boş bir değer alabilir.
    price= models.DecimalField(max_digits=10, decimal_places=2) #bu decimal fiyat alanının max karakteri 10 basamaklı olsun, virgünden sonraki kısım 2 basamaklı olsun.
    stock = models.PositiveIntegerField(default=0)
    slug= models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    #veriyi temsil etme--> ürünlerin isimleri gelsin
    def __str__(self):
        return self.name