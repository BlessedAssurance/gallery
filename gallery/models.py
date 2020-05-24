from django.db import models

# Create your models here.

# IMAGES
class Images (models.Model):
    name= models.CharField(max_length =30)
    description = models.CharField(max_length =100)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

