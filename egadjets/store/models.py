from django.db import models

# Create your models here.
class product(models.Model):
     name=models.CharField(max_length=100)
     price=models.IntegerField()
     image=models.ImageField(upload_to="product_images")
     description=models.CharField(max_length=100)
     category=models.CharField(max_length=100)


     