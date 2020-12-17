from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/product-list/',
        'Detail View':'/product-list/<str:pk>',
        'Create':'/product-create',
        'Update':'/product-update/<str:pk>',
        'Delete':'/product-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def productList(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request,pk):
    products=Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request,pk):
    product=Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product,data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return Response("Item deleted successfully")

