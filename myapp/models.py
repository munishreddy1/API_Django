from django.db import models

# Create your models here.
#Created a model or schema with name Product
class Product(models.Model):

    def __str__(self) -> str:
        return self.name 
    
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200)

