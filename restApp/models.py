from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

# Create your models here.



class Product(models.Model):
    product_id  = models.IntegerField(unique=True)
    p_name = models.CharField(max_length=225)
    p_brand = models.CharField(max_length=225)
    production_date = models.DateField(validators=[MaxValueValidator(datetime.date.today)])
    price = models.FloatField()
    expiration_date = models.DateField(default=datetime.date.today)
