from django.db import models
class lunette(models.Model):
    types = models.CharField(max_length=255)
    photo = models.ImageField()
    

# Create your models here.
                           