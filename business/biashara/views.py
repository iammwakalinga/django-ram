from django.shortcuts import render
from rest_framework import generics
from .serializers import categoryserializer,Bookserializer,Productserializer
from .models import category,Book,Product

class Listcategory(generics.ListCreateAPIView):
    queryset=category.objects.all()
    serializer_class=categoryserializer

class Detailcategory(generics.RetrieveUpdateDestroyAPIView):
   queryset=category.objects.all()
   serializer_class=categoryserializer

class ListBook(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=Bookserializer

    
class DetailBook(generics.RetrieveUpdateDestroyAPIView):
   queryset=Book.objects.all()
   serializer_class=Bookserializer


class ListProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer



