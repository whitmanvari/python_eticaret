from django.urls import path
from .views import CatalogCategoryList, AdminCategoryList, CatalogCategoryDetails, AdminCategoryDetails,AdminCategoryCreate,AdminCategoryEdit, AdminCategoryDelete

urlpatterns = [
    path('', CatalogCategoryList.as_view(), name='catalog_category_list'),
    path('admin/', AdminCategoryList.as_view(), name='admin_category_list'),
    path('<int:pk>', CatalogCategoryDetails.as_view(), name='catalog_category_details'),
    path('admin/<int:pk>/', AdminCategoryDetails.as_view(), name='admin_category_details'),
    path('admin/create/', AdminCategoryCreate.as_view(), name='admin_create_category'),
    path('admin/<int:pk>/edit/', AdminCategoryEdit.as_view(), name='admin_edit_category'),
    path('admin/<int:pk>/delete/', AdminCategoryDelete.as_view(), name='admin_delete_category'),
]
