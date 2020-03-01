from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    campany = models.CharField(max_length=100,blank=False)
    rate = models.CharField(max_length=100,blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=100,blank=False)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    debit = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
