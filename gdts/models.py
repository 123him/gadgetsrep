from django.db import models

# Create your models here.
class tbl_user1(models.Model):
    username=models.CharField(max_length=50)
    
    first_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    photo=models.URLField(max_length=200)
    address=models.CharField(max_length=500)
    
    class Meta:
        db_table='tbl_user1'

class tbl_products(models.Model):
    product_name=models.CharField(max_length=50)
    photo=models.URLField(max_length=300)
    price=models.IntegerField()
    color=models.CharField(max_length=50)
    warranty=models.IntegerField()
    
    
    class Meta:
        db_table='tbl_products'