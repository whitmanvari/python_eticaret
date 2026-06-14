from django.urls import path
from .views import CategoryListAV, CategoryDetailsAV
#app'le ilgili url'leri alacağımız alan. 
urlpatterns = [
    path('', CategoryListAV.as_view(), name='categories'),
    path('<int:pk>', CategoryDetailsAV.as_view(), name='category_details'),
]