from django.db import models


COPY_CHOICES = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
]

class Products(models.Model):
    image=models.ImageField(upload_to='static/photos/',default=None)
    description=models.CharField(max_length=100)
    price=models.FloatField()
    title=models.CharField(max_length=100)
    copies =models.CharField(max_length=56, choices=COPY_CHOICES)
    
    def __str__(self):
        return str(self.id)

# Create your models here.
