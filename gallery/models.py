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

#LOCATION
class Location(models.Model):
    locations=(
        ('Kenya','Kenya'),
        ('Uganda','Uganda'),
        ('Paris','Paris'),
        ('London','London'),
        ('Mexico','Mexico'),
        ('India','India'),
    )
    locs = models.CharField(max_length = 255, choices = locations)

    class Meta:
        verbose_name_plural = 'Location'
    

def __str__(self):
        return f"{self.locs}"


#CATEGORY
class Category(models.Model):
    categories = (
        ('Flowers','Flowers'),
        ('Articles','Articles'),
        ('Animals','Animals'),
        ('People','People')
    )
    cate = models.CharField(max_length = 255, choices = categories)
    class Meta:
        verbose_name_plural = 'categories'



    def __str__(self):
        return f"{self.cate}"