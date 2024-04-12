from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    about = models.TextField()
    category = models.CharField(max_length=255)
    gbjoy = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/')
    price = models.IntegerField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=200)
    

    def __str__(self) -> str:
        return self.name