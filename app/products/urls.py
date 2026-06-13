from django.urls import path
from .views import product_list
#app'le ilgili url'leri alacağımız alan. 
urlpatterns = [
    path('list/', product_list, name='products')

]