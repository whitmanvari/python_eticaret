from django.urls import path
from .views import CommentList, CommentCreate, CommentEdit, CommentDelete, AdminCommentList, AdminCommentEdit, AdminCommentDelete

urlpatterns = [
    path('product/<int:pk>/', CommentList.as_view(), name='comment_list'),
    path('<int:pk>/create/', CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/edit/',CommentEdit.as_view(), name='comment_edit'),
    path('<int:pk>/delete/',CommentDelete.as_view(), name='comment_delete'),

    path('admin/', AdminCommentList.as_view(), name='admin_comment_list'),
    path('admin/product/<int:pk>/', AdminCommentList.as_view(), name='admin_comment_list_product'),
    path('admin/<int:pk>/edit/',AdminCommentEdit.as_view(), name='admin_comment_edit'),
    path('admin/<int:pk>/delete/',AdminCommentDelete.as_view(), name='admin_comment_delete')
   
]

#api/comments/product/1 --> product comment listesi
#api/comments/1/create  -->  comment ekleme
#api/comments/1/edit    -->  comment güncelleme
#api/comments/1/delete  -->  comment silme

#api/comments/admin --> Admin comment listesi
#api/commments/admin/product/1 --> Admin comment listesi (product bazlı)
#api/comments/admin/1/edit --> Admin comment güncelleme
#api/comments/admin/1/delete --> Admin comment silme
