from django.db import models

# Create your models here.


#Created a model/schema with name Product in inbuilt database
class Product(models.Model): #inherited the models.Model inbuilt django function for enabling ORM 

    #String representation for the instance of this model with the name variable
    def __str__(self) -> str:
        return self.name 
    
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200)

