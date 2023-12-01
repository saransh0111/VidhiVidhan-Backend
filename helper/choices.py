from helper import keys
from django.db import models

class ProductTypeChoices(models.Choices):
        INDOOR = keys.INDOOR
        OUTDOOR = keys.OUTDOOR
