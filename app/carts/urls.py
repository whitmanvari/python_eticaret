from django.urls import path
from .views import AddToCartView, CartDetailView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/', AddToCartView.as_view(), name='cart_add'),
    # path('update/<int:item_id>/', UpdateCartItemView.as_view(), name='cart_item_update'),
    # path('delete/<int:item_id>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
]
