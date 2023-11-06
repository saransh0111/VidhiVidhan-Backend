from rest_framework import serializers
from users.models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id','user','full_name','profile_image','address','pin_code']