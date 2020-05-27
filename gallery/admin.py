from django.contrib import admin
from .models import Images, Location, Category

# Register your models here.
admin.site.register(Images)
admin.site.register(Location)
admin.site.register(Category)



# export DB_NAME= 'gallery'
# export DB_USER= 'vincent'
# export DB_PASSWORD= '29484510'
# export SECRET_KEY= 'e!g$6q44=v%67^6bh1of!vymkt+9kyf*_t(u4vt99-lh(c5krl'
# DEBUG = True

