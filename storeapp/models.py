from django.db import models

# Create your models here.

class items(models.Model):
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField()
    item_disc=models.CharField(max_length=100)
    

class cart(models.Model):
    items=models.ManyToManyField(items)
    quantity=models.IntegerField()
    


