from django.urls import path
from .views import Listcategory,Detailcategory,ListBook,DetailBook,ListProduct,DetailProduct

urlpatterns=[
    path('categories',Listcategory.as_view(), name='category'),
    path('categories/<int:pk>/',Detailcategory.as_view() ,name='singlecategory'),
    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>/',DetailBook.as_view(),name='singlebook'),
    path('products',ListProduct.as_view(),name='product'),
    path('products<int:pk>/',DetailProduct.as_view(),name='singleproduct'),

]