from django.urls import path
from .views import CommentList, CommentCreate
# CommentDelete,CommentEdit

urlpatterns = [
    path('product/<int:pk>', CommentList.as_view(), name='comment_list'),
    path('<int:pk>/create', CommentCreate.as_view(), name='comment_create')
    #path('<int:pk>/delete',CommentDelete.as_view(), name='comment_delete'),
    #path('<int:pk>/edit',CommentEdit.as_view(), name='comment_edit')
]

#comments/product/1 --> product comment listesi
#comments/1/create  -->  comment ekleme
#comments/1/edit    -->  comment güncelleme
#comments/1/delete  -->  comment silme
