from django.db import models
from ckeditor.fields import RichTextField

class main_services(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/images/main")
    description = RichTextField()




class banners(models.Model):
    image1 = models.ImageField(upload_to="media/images/main/banners", null=True)
    image2 = models.ImageField(upload_to="media/images/main/banners", null=True)
    image3 = models.ImageField(upload_to="media/images/main/banners", null=True)