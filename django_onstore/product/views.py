from django.shortcuts import render, resolve_url
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.models import User
from base64 import standard_b64decode

from rest_framework import serializers
from rest_framework import serializers, status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Category, Product
from .serializers import  ProductSerializer,CategorySerializer

class LatestProcductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) |   Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    return Response({"products":[]})

@api_view(['POST'])
def additem(request):
    category_name = request.data.get('category')
    username_post = request.data.get('username')
    name = request.data.get('name')
    slug = request.data.get('slug')
    price = request.data.get('price')
    description = request.data.get('description')
    product = Product()
    category = Category.objects.get(name=category_name)
    username = User.objects.get(username=username_post)
    if category and name and price and category:
        product.category = category
        product.name = name
        product.username = username
        product.description = description
        product.slug = slug
        product.price = price
        product.image_1 = request.data.get('image0')
        product.image_2 = request.data.get('image1')
        product.image_3 = request.data.get('image2')
        product.image_4 = request.data.get('image3')
        Product.save(product)
        return Response("Done")
    return Response("Error happened")

@api_view(['POST'])
def deleteitem(request):
    username_post = request.data.get('username')
    username = User.objects.get(username=username_post)
    if username is not None:
        instance = Product.objects.filter(username=username)
        instance.delete()
        return Response("Done")
    return Response("Error")


@api_view(['POST'])
def updateitem(request):
    username_post = request.data.get('username')
    name = request.data.get('name')
    description = request.data.get('description')
    price = request.data.get('price')
    category_post = request.data.get('category')
    username = User.objects.get(username=username_post)
    category = Category.objects.get(name=category_post)
    if username is not None:
        instance = Product.objects.get(username=username)
        if name is not None:
            instance.name = name
        if description is not None:
            instance.description = description
        if price is not None:
            instance.price = price
        if category is not None:
            instance.category = category
        instance.save()
        return Response("Done")
    return Response("Error")


class ProductsList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        products = Product.objects.filter(username=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)