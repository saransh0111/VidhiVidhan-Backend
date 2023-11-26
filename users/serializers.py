from rest_framework import serializers
from helper import keys, messages
from users.models import Customer, OTPManager, Pandit, User, ShopOwner

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id','user','full_name','profile_image','address','pin_code']


class SignUpSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100)
    profile_image = serializers.FileField()
    address = serializers.CharField()
    pin_code = serializers.CharField()

    class Meta:
        model = User
        fields = ['mobile','full_name','profile_image','address','pin_code']

class VerifyOTPSerializer(serializers.ModelSerializer):
    """ SERIALIZER FOR VERIFYING OTPs """
    mobile = serializers.CharField(max_length=10,write_only=True, required=True,error_messages={keys.MAX_LENGTH: messages.ENSURE_10_CHAR,keys.REQUIRED:messages.MOBILE_REQUIRED,keys.BLANK:messages.MOBILE_REQUIRED})
    otp = serializers.CharField(max_length=4, write_only=True, required=True, error_messages={keys.MAX_LENGTH: messages.ENSURE_4_CHAR, keys.REQUIRED: messages.MOBILE_OTP_REQUIRED, keys.BLANK: messages.MOBILE_OTP_REQUIRED})
    
    class Meta:
        model = OTPManager
        fields = ['mobile', 'otp']

class ResendOTPSerializer(serializers.ModelSerializer):
    """ SERIALIZER FOR RESENDING OTPs """
    mobile = serializers.CharField(max_length=10,write_only=True, required=True,error_messages={keys.MAX_LENGTH: messages.ENSURE_10_CHAR,keys.REQUIRED:messages.MOBILE_REQUIRED,keys.BLANK:messages.MOBILE_REQUIRED})
    
    class Meta:
        model = OTPManager
        fields = ['mobile']

class UserProfileSerializer(serializers.Serializer):
    """ SERIALIZER FOR USER PROFILE """
    
    class Meta:
        model = User
        fields = ['mobile']

class ShopOwnerSerializer(serializers.Serializer):
    """ SERIALIZER FOR SHOP OWNER """

    class Meta:
        model = ShopOwner
        fields = ['shop_name', 'profile_image', 'address', 'description']

class PanditSerializer(serializers.Serializer):
    """ SERIALIZER FOR PANDIT """

    class Meta:
        model = Pandit
        fields = ['name', 'profile_image', 'price']