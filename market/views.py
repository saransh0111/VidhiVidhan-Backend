from django.shortcuts import render
from helper import messages
from helper.functions import ProductFunctions, ResponseHandling
from rest_framework.response import Response
from market.serializers import ProductSerializer
from rest_framework import generics
from helper import *
# Create your views here.

class ListProductsAPIView(generics.ListAPIView):
    """
    API to list all products

    HEAD PARAM: JWT Token
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Dictionary
    """
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset  = ProductFunctions.get_all_product.order_by('-created')
        if not queryset:
            return Response(ResponseHandling.failure_response_message(messages.NO_DATA_AVAILABLE, []), status=status200)
        products = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, products.data), status=status200)
    