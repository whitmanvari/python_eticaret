from django.urls import path
from .views import CommentListView, CommentListByProductView, CommentDetailsView

urlpatterns = [
    path('', CommentListView.as_view(), name='comments'),
    path('<int:pk>/product', CommentListByProductView.as_view(), name='comments_by_product'),
    path('<int:pk>', CommentDetailsView.as_view(), name='comments_details')
]
