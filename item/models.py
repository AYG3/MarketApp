from django.contrib.auth.models import User
from django.db import models

#After creating a new class
#python mange.py makemigrations
#python manage.py migrate
#register class in admin interface

#Configure for media files like images in setting.py:
# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    #To correct Categorys spelling in admin dashboard
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    #To show the name in admin 
    def __str__(self):
        return self.name
    
    # https://youtu.be/ZxMB6Njs3ck?t=2001
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name