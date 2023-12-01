import re
from rest_framework import status
import random
from django.conf import settings
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from market.models import Products
from users.models import Customer, OTPManager, Pandit, ShopOwner, User


class ResponseHandling:
    def failure_response_message(detail,result):
        """
        error message for failure
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}

    def success_response_message(detail,result):
        """
        success message for Success
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}

#-------------------------- STATUS CODE ---------------------------

status200 = status.HTTP_200_OK
status201 = status.HTTP_201_CREATED
status202 = status.HTTP_202_ACCEPTED
status204 = status.HTTP_204_NO_CONTENT
status400 = status.HTTP_400_BAD_REQUEST
status401 = status.HTTP_401_UNAUTHORIZED
status404 = status.HTTP_404_NOT_FOUND

#-------------------------------------- ERROR GENERAL FUNCTIONS ------------------------------------

def error_message_function(errors):
    """
    return error message when serializer is not valid
    :param errors: error object
    :returns: string
    """
    for key, values in errors.items():
        error = [value[:] for value in values]
        err = ' '.join(map(str,error))
        return err
    
#------------------ TO Generate Random OTP ------------------------
def generate_otp():
    """
    returns 6 digit random number
    """
    otp = random.randint(100000, 999999)
    return otp


#------------------ To create user token for authentication ------------
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }    


def isMobileValid(mobile):
    Pattern = re.compile("^[6-9][0-9]{9}$")
    return Pattern.match(mobile)
    
def isEmailValid(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pattern,email):
      return True
    return False



#---------------- USER FUNCTIONS -----------------

class UserFunctions:
    
    def get_all_user():
        """
        gives queryset of all users
        return queryset
        """
        queryset = User.objects.all()
        return queryset
    
    def check_is_mobile_exist(mobile):
        """
        To check is mobile already registered or not
        params mobile: mobile of user 
        result: queryset
        """
        queryset = User.objects.filter(mobile=mobile)
        return queryset
    
    def get_user_by_id(id):
        """
        To get user object by user id
        params mobile: id of user
        result: object
        """
        user_obj = User.objects.filter(id=id)
        return user_obj
    
    def get_user_by_mobile(mobile):
        """
        To get user object by mobile number
        params mobile: mobile of user 
        result: object
        """
        user_obj = User.objects.get(mobile=mobile)
        return user_obj
    
    def check_mobile_in_OTPManager(mobile):
        """
        To check is mobile already registered or not
        params mobile: mobile of user 
        result: queryset
        """
        queryset = OTPManager.objects.filter(mobile=mobile)
        return queryset
    
    def create_entry_in_OTPManager(mobile, otp):
        """
        To create an entry if user does not exists
        params mobile: otp
        result: object
        """
        user_otp = OTPManager.objects.create(mobile=mobile,otp=otp)
        return user_otp

#---------------- USER FUNCTIONS -----------------

class UserFunctions:
    
    def get_all_user():
        """
        gives queryset of all users
        return queryset
        """
        queryset = User.objects.all()
        return queryset
    
    def check_is_mobile_exist(mobile):
        """
        To check is mobile already registered or not
        params mobile: mobile of user 
        result: queryset
        """
        queryset = User.objects.filter(mobile=mobile)
        return queryset
    
    def get_user_by_id(id):
        """
        To get user object by user id
        params mobile: id of user
        result: object
        """
        user_obj = User.objects.filter(id=id)
        return user_obj
    
    def get_user_by_mobile(mobile):
        """
        To get user object by mobile number
        params mobile: mobile of user 
        result: object
        """
        user_obj = User.objects.get(mobile=mobile)
        return user_obj
    
    def check_mobile_in_OTPManager(mobile):
        """
        To check is mobile already registered or not
        params mobile: mobile of user 
        result: queryset
        """
        queryset = OTPManager.objects.filter(mobile=mobile)
        return queryset
    
    def create_entry_in_OTPManager(mobile, otp):
        """
        To create an entry if user does not exists
        params mobile: otp
        result: object
        """
        user_otp = OTPManager.objects.create(mobile=mobile,otp=otp)
        return user_otp
    
    
#--------------------- CUSTOMER FUNCTIONS --------------

class CustomerFunctions:
    
    def get_customer_by_user(user_obj):
        """
        gives object of customer by it's user
        :returns: object
        """
        object = Customer.objects.filter(user=user_obj).first()
        return object
    
    
    
#--------------------- OWNER FUNCTIONS --------------

class OwnerFunctions:

    def get_customer_by_user(user_obj):
        """
        gives object of owner by it's user
        :returns: object
        """
        object = ShopOwner.objects.filter(user=user_obj).first()
        return object
    
    def get_shopowner_by_user(user_obj):
        """
        gives object of shop owner by it's user
        :returns: object
        """
        object = ShopOwner.objects.filter(user=user_obj).first()
        return object
    

class ProductFunctions:

    def get_all_product():
        queryset = Products.objects.all()
        return queryset
    

class ShopFunctions:
    def get_all_shop():
        queryset = ShopOwner.objects.all()
        return queryset
    
class PanditFunctions:
    def get_all_pandit():
        queryset = Pandit.objects.all()
        return queryset