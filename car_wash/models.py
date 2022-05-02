from datetime import datetime
from django.db import models

# Create your models here.


class AllNfts(models.Model):
    uri=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    status=models.CharField(max_length=20)
    itemid=models.IntegerField(null=True)
    datetime=models.DateTimeField(auto_now_add=True)
