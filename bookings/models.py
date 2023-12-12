from django.db import models
from appproducts.models import Products
from django.contrib.auth.models import User

class Bookings(models.Model):
    productid= models.ForeignKey(Products,on_delete=models.CASCADE)  
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    bookingdate=models.DateTimeField()
    cost=models.FloatField(null=True,blank=True)
    quantity=models.IntegerField()
    isdelivered=models.BooleanField()
    
    def __str__(self):
        return str(self.id)

# Create your models here.
