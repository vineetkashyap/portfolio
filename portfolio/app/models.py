from django.db import models
class Product(models.Model):
    title=models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='productimg')