from django.db import models
from django.conf import settings
from products.models import Product

#carts modeli, cart içerisinde ona bağlı ürünler olacak. cart_item tablosu da oluşturacağım.

class Cart(models.Model):
    #userı sildiğimde cart silinsin.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s Cart"
    
    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        return total
    
class CartItem(models.Model):
    #cartı sildiğimde cart_item silinsin. productı sildiğimde cart_item silinsin.
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_price(self):
        return self.quantity * self.product.price
    
    class Meta:
        unique_together = ('cart', 'product')
