from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Defined a viewset for handling Product-related operations.
# This viewset is protected by TokenAuthentication, and only authenticated users (IsAuthenticated) can access it.
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() # Define the queryset to retrieve all Product objects from the database.
    serializer_class = ProductSerializer # Use the ProductSerializer to serialize and deserialize Product objects.

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class FashionViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve Product objects with the category 'fashion' from the database.
    queryset = Product.objects.filter(category='fashion')    
    serializer_class = ProductSerializer

class SportsViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve Product objects with the category 'sports' from the database.
    queryset = Product.objects.filter(category='sports')
    serializer_class = ProductSerializer

class ElectronicsViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve Product objects with the category 'electronics' from the database.
    queryset = Product.objects.filter(category='electronics')
    serializer_class = ProductSerializer