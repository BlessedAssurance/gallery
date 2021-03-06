from django.db import models

# Create your models here.

# IMAGES
class Images (models.Model):
    name= models.CharField(max_length =30)
    image=models.ImageField(upload_to ='images/', null=True)
    description = models.TextField()
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE,null=True)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE,null=True)

    @classmethod
    def search_image(cls,category):
        images = cls.objects.filter(image_category__name =category )
        
        return images
    
    @classmethod 
    def get_all_images(cls):
        images=cls.objects.all()
        return images
    
    @classmethod
    def save_image(self):
        self.save()
        
    @classmethod
    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image.value)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    
    @classmethod
    def filter_by_location(cls,location):
        images_location = cls.objects.filter(image_location_name=location)
        return images_location

    def __str__(self):
        return self.name
    # class Meta:
    #     ordering = ['name']

# #LOCATION
# class Location(models.Model):
#     locations=(
#         ('Kenya','Kenya'),
#         ('Uganda','Uganda'),
#         ('Paris','Paris'),
#         ('London','London'),
#         ('Mexico','Mexico'),
#         ('India','India'),
#     )
#     locs = models.CharField(max_length = 255, choices = locations)

#     class Meta:
#         verbose_name_plural = 'Location'
#     @classmethod
#     def save_location(self):
#         self.save()
    
#     @classmethod 
#     def delete_location(self):
#         self.delete()
        
#     @classmethod
#     def update_locs(cls, id, new_locs):
#         cls.objects.filter(id=id).update(locs=new_locs)
    

# def __str__(self):
#         return f"{self.locs}"

#CATEGORY
class Location(models.Model):
    Places = (
        ('Kenya','Kenya'),
        ('Uganda','Uganda'),
        ('Paris','Paris'),
        ('London','London'),
        ('Mexico','Mexico'),
        ('India','India'),
    )
    locs = models.CharField(max_length = 255, choices = Places )
    class Meta:
        verbose_name_plural = 'location'

    @classmethod
    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(self):
        self.delete()
        
    @classmethod
    def update_cate(cls, id, new_cate):
        cls.objects.filter(id=id).update(locs=new_cate)


    def __str__(self):
        return f"{self.locs}"




#CATEGORY
class Category(models.Model):
    categories = (
        ('Flowers','Flowers'),
        ('Places','Places'),
        ('Animals','Animals'),
        ('People','People')
    )
    cate = models.CharField(max_length = 255, choices = categories)
    class Meta:
        verbose_name_plural = 'categories'

    @classmethod
    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(self):
        self.delete()
        
    @classmethod
    def update_cate(cls, id, new_cate):
        cls.objects.filter(id=id).update(cate=new_cate)


    def __str__(self):
        return f"{self.cate}"