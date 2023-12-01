from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from helper import keys
from helper.functions import *
from helper import messages
from users.models import *
from rest_framework import generics
from users.serializers import  CustomerSerializer, PanditSerializer, ShopOwnerSerializer, SignUpSerializer, UserProfileSerializer, VerifyOTPSerializer, ResendOTPSerializer
from rest_framework.response import Response
from helper.swagger_openapi import *

from rest_framework.permissions import IsAuthenticated

# swagger imports
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SendOTP(generics.GenericAPIView):
    """ 
    API to send OTP to mobile number
    
    HEAD PARAM: None
    PATH PARAMS: None
    REQUEST BODY PARAM: Mobile
    API RESPONSE: Dictionary
    """
    serializer_class = SignUpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            errors = serializer.errors
            err = error_message_function(errors)
            return Response(ResponseHandling.failure_response_message(err, {}), status=status400)
        mobile = request.data[keys.MOBILE]
        if mobile is None :
            return Response(ResponseHandling.failure_response_message(messages.ENTER_VALID_NUMBER, ""), status=status400)
        if not isMobileValid(mobile):
            return Response(ResponseHandling.failure_response_message(messages.ENTER_VALID_NUMBER, ""), status=status400)
        # otp = generate_otp()
        mobile_number = str(mobile)
        otp = mobile_number[:4]
        is_mobile_number_in_OTPManager = UserFunctions.check_mobile_in_OTPManager(mobile)
        if is_mobile_number_in_OTPManager.exists():
            is_mobile_number_in_OTPManager.delete()
        UserFunctions.create_entry_in_OTPManager(mobile,otp)
        if not UserFunctions.check_is_mobile_exist(mobile):
            User.objects.create(mobile=mobile)
        return Response(ResponseHandling.success_response_message(messages.OTP_TOKEN_SUCCESFULLY_SENT, ""), status=status200)   
    
class VerifyOTP(generics.GenericAPIView):
    """ 
    API to verify OTP sent to mobile number
    
    HEAD PARAM: None
    PATH PARAMS: None
    QUERYSTRING PARAMS: Mobile and OTP
    API RESPONSE: Dictionary
    """
    serializer_class = VerifyOTPSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            errors = serializer.errors
            err = error_message_function(errors)
            return Response(ResponseHandling.failure_response_message(err, {}), status=status400)
        mobile = request.data[keys.MOBILE]
        otp = request.data[keys.OTP]
        
        if not isMobileValid(mobile):
            return Response(ResponseHandling.failure_response_message(messages.ENTER_VALID_NUMBER, ""), status=status400)
        is_mobile_in_OTPManager = UserFunctions.check_mobile_in_OTPManager(mobile)
        if is_mobile_in_OTPManager.exists():
            is_mobile_in_OTPManager = is_mobile_in_OTPManager.first()
            store_mobile_otp = is_mobile_in_OTPManager.otp
            if str(store_mobile_otp) == str(otp):
                is_mobile_in_OTPManager.delete()
                user = UserFunctions.get_user_by_mobile(mobile)
                token = get_tokens_for_user(user)
                return Response(ResponseHandling.success_response_message(messages.OTP_MATCHED_REGISTRATION, {"token":token}), status=status200)
            else:
                return Response(ResponseHandling.failure_response_message(messages.OTP_INCORRECT, {}), status=status400)
        else:
            return Response(ResponseHandling.failure_response_message(messages.MOBILE_NOT_RECONGNISED, {}), status=status400)     

class ResendOTP(generics.GenericAPIView):
    """ 
    API to resend OTP to mobile number
    
    HEAD PARAM: None
    PATH PARAMS: None
    QUERYSTRING PARAMS: Mobile
    API RESPONSE: Dictionary
    """
    serializer_class = ResendOTPSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            errors = serializer.errors
            err = error_message_function(errors)
            return Response(ResponseHandling.failure_response_message(err, {}), status=status400)
        mobile = request.data[keys.MOBILE]
        is_mobile_in_OTPManager = UserFunctions.check_mobile_in_OTPManager(mobile)
        if is_mobile_in_OTPManager.exists():
            # new_otp = generate_otp()
            # otp = generate_otp()
            mobile_number = str(mobile)
            new_otp = mobile_number[:4]
            is_otp_update = is_mobile_in_OTPManager.update(otp=new_otp)
            if is_otp_update:
                return Response(ResponseHandling.success_response_message(messages.OTP_TOKEN_SUCCESFULLY_SENT, {}), status=status200)
            else:
                return Response(ResponseHandling.failure_response_message(messages.MOBILE_NOT_RECONGNISED, {}),status=status400)
        else:
            return Response(ResponseHandling.failure_response_message(messages.MOBILE_NOT_RECONGNISED, {}), status=status400)

# This need to change according to user

class GetUserProfileAPI(generics.RetrieveAPIView):
    """ 
    API to get user profile data
    
    HEAD PARAM: JWT Token
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Dictionary or None
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        data = {'mobile': user.mobile}
        
        if user.user_type == keys.CUSTOMER:
            customer_obj = CustomerFunctions.get_customer_by_user(user)
            data['profile_image'] = customer_obj.profile_image if customer_obj else None
            data['full_name'] = customer_obj.full_name if customer_obj else None
        elif user.user_type == keys.OWNER:
            owner_obj = OwnerFunctions.get_shopowner_by_user(user)
            data['profile_image'] = owner_obj.profile_image if owner_obj else None
            data['shop_name'] = owner_obj.shop_name if owner_obj else None
        else:
            data['profile_image'] = None
            data['full_name'] = keys.UNKNOWN
            
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, {'data':data}), status=status200)

class ListShopsAPIView(generics.ListAPIView):
    """
    API to list all shops

    HEAD PARAM: JWT Token
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Dictionary
    """
    serializer_class = ShopOwnerSerializer
    # permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset  = ShopFunctions.get_all_shop.order_by('-created')
        if not queryset:
            return Response(ResponseHandling.failure_response_message(messages.NO_DATA_AVAILABLE, []), status=status200)
        shops = ShopOwnerSerializer(queryset, many=True, context={'request': request})
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, shops.data), status=status200)
    

class ListPanditsAPIView(generics.ListAPIView):
    """
    API to list all pandits

    HEAD PARAM: JWT Token
    PATH PARAMS: None
    QUERYSTRING PARAMS: None
    API RESPONSE: Dictionary
    """
    serializer_class = PanditSerializer
    # permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset  = PanditFunctions.get_all_pandit.order_by('-created')
        if not queryset:
            return Response(ResponseHandling.failure_response_message(messages.NO_DATA_AVAILABLE, []), status=status200)
        pandits = PanditSerializer(queryset, many=True, context={'request': request})
        return Response(ResponseHandling.success_response_message(messages.OPERATION_SUCCESS, pandits.data), status=status200)
    
class CustomerViewSet(viewsets.ModelViewSet):
 permission_classes = [IsAuthenticated]
 queryset = Customer.objects.all()
 serializer_class = CustomerSerializer


