from django.shortcuts import render
from django.http import JsonResponse
from .models import Soda
from .serializers import SodaSerializer
from rest_framework.decorators import api_views
from rest_framework.response import Response
from rest_framework.response import status

@api_views(['GET','POST'])
def drink_list(request):

    if request.method == 'GET':
      drinks = Soda.objects.all()
      serializer = SodaSerializer(drinks,many = True)
      return JsonResponse({"drinks":serializer.data},safe=False)

    if request.method == 'POST':
       serializer= SodaSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer, status=status.HTTP_201_CREATED)


