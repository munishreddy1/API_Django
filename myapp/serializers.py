from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Product          # The model to be serialized
        fields = '__all__'       # Included all the fields in the serialized representation

