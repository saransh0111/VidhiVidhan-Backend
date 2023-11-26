from rest_framework import serializers
from market.models import *

class ProductSerializer(serializers.ModelSerializer):
    """ SERIALIZER FOR PRODUCT """
    
    class Meta:
        model = Products
        fields = ['product_name', 'product_image', 'price', 'category', 'created']
       