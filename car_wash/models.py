from datetime import datetime
from django.db import models

# Create your models here.


class AllNfts(models.Model):
    uri=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    status=models.CharField(max_length=20)
    itemid=models.IntegerField(null=True)
    owner=models.CharField(max_length=255,null=True)
    seller=models.CharField(max_length=255,null=True)
    datetime=models.DateTimeField(auto_now_add=True)

class Nftuser(models.Model):
    username = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    cover_pic=models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    datetime=models.DateTimeField(auto_now_add=True)
