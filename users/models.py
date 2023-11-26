from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
from django.contrib.auth.models import PermissionsMixin
from helper import keys

from helper.models import CreationModificationBase

class UserManager(BaseUserManager):
    def _create_user(self, mobile, password, is_staff, is_superuser, **extra_fields):
        if not mobile:
            raise ValueError('Users must have a mobile number')
        current = now()
        user = self.model(
            mobile=mobile,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=current,
            date_joined=current,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, mobile=None, password=None, **extra_fields):
        self.set_password(password)
        self.save(using=self._db)
        return self._create_user(mobile, password, False, False, **extra_fields)
    
    def create_staff_user(self, mobile, password=None, **extra_fields):
        return self._create_user(mobile, password, True, False, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        user = self._create_user(mobile, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
       
class User(AbstractBaseUser,PermissionsMixin):
    """ User Model """
                                
    mobile = models.CharField(max_length = 10, null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=100, default=None, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = UserManager()
    

    def __str__(self):
        return f'{self.mobile}'
    
class Customer(CreationModificationBase):
    user = models.OneToOneField(to="users.User", on_delete=models.CASCADE, related_name='_customer')
    profile_image = models.FileField(upload_to='user/profile/',blank=True,null=True)
    full_name =  models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100, blank=True,null=True)
    is_new = models.BooleanField(default=False, help_text='detail of this user is not filled')
    pin_code = models.CharField(max_length=100,blank=True,null=True)
        
    def __str__(self):
        return f'{self.full_name}'
    
class ShopOwner(CreationModificationBase):
    user = models.OneToOneField(to="users.User", on_delete=models.CASCADE, related_name='_owner')
    profile_image = models.FileField(upload_to='user/profile/',blank=True,null=True)
    shop_name =  models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100, blank=True,null=True)
    description = models.CharField(max_length=200, blank=True,null=True)
    is_new = models.BooleanField(default=False, help_text='detail of this user is not filled')
    pin_code = models.CharField(max_length=100,blank=True,null=True)
    products = models.ManyToManyField("market.Products", verbose_name="shop products")
        
    def __str__(self):
        return f'{self.shop_name}'
    
class Pandit(CreationModificationBase):
    name = models.CharField(max_length=100,blank=True,null=True)
    profile_image = models.FileField(upload_to='user/profile/',blank=True,null=True)
    price = models.FloatField(max_length=100, verbose_name="pandit price for booking")
    
class OTPManager(CreationModificationBase):
    ''' This model store mobile number and OTP so that it can be used for validation '''
    mobile = models.CharField(max_length = 10, unique = True)
    otp = models.CharField(max_length = 4, blank=True, null=True)
    count = models.IntegerField(default=0, help_text="Count of OTP sent")
    
    class Meta:
        verbose_name = keys.OTP_MANAGER
        verbose_name_plural = keys.OTP_MANAGERS

    def __str__(self):
        return str(self.otp) + ' OTP is sent to ' + str(self.mobile)
