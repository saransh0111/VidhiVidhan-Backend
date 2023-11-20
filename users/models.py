from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
from django.contrib.auth.models import PermissionsMixin

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
    
class Customer(models.Model):
    user = models.OneToOneField(to="users.User", on_delete=models.CASCADE, related_name='_customer')
    profile_image = models.FileField(upload_to='user/profile/',blank=True,null=True)
    full_name =  models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100, blank=True,null=True)
    is_new = models.BooleanField(default=False, help_text='detail of this user is not filled')
    pin_code = models.CharField(max_length=100,blank=True,null=True)
        
    def __str__(self):
        return f'{self.full_name}'
    
