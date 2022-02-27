
from django.http import Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductsSerializer, CategorySerializer
from rest_framework.decorators import api_view


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(
            category_slug=category_slug, product_slug=product_slug)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({products:[]})
 