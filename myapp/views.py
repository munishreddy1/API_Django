from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class FashionViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(category='fashion')
    serializer_class = ProductSerializer

class SportsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(category='sports')
    serializer_class = ProductSerializer

class ElectronicsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(category='electronics')
    serializer_class = ProductSerializer