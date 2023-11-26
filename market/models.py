from django.db import models
from helper import keys
from helper.choices import ProductTypeChoices
from helper.models import CreationModificationBase


class Products(CreationModificationBase):
    """ This model will store products and their details """

    product_name = models.CharField(max_length=150, verbose_name="product name")
    product_image = models.ImageField(upload_to=keys.MEDIA_FOLDERS_DICT.get(keys.PRODUCT_IMAGE),verbose_name="product image")
    price = models.FloatField(max_length=100, verbose_name="product price")
    category = models.CharField(max_length=55, choices=ProductTypeChoices.choices,default=None, blank=True, null=True)

  