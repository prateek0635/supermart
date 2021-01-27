from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import items,cart
from .serializers import itemsSerializers,cartSerializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# Create your views here.


class itemView(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        item=items.objects.all()
        serializer=itemsSerializers(item,many=True)
        return Response(serializer.data)


    def post(self,request):

        serializer = itemsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class cartView(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        cart_item=cart.objects.all()
        serializer=cartSerializers(cart_item,many=True)
        return Response(serializer.data)


    def post(self,request):

        serializer = cartSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class itemDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return items.objects.get(pk=pk)
#         except items.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

#     def get(self, request, pk):
#         item = self.get_object(pk)
#         serializer = itemsSerializers(item)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         item = self.get_object(pk)
#         serializer = itemsSerializers(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         item = self.get_object(pk)
#         item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, int):
    
    try:
        item = items.objects.get(pk=int)
    except items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = itemsSerializers(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = itemsSerializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)