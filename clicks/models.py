from enum import unique
from django.db import models
from django.template.defaultfilters import  title
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse
from cloudinary.models import CloudinaryField



# Create your models here.
class Category(models.Model):
    title = models.CharField(null=True,blank=True,max_length=200)
    uniqueId =models.CharField(null=True,blank=True,max_length=200)
    date_created = models.DateTimeField(blank=True,null=True)
    last_updated = models.DateTimeField(blank=True,null=True)

    @classmethod  
    def search_by_category(cls,search_term):
        category = cls.objects.filter(title__icontains=search_term)
        return category 

    def __str__(self):
        return '{} {}'.format(self.title,self.uniqueId)

    def get_absolute_url(self):
        return reverse('category-detail',kwargs={''})   

    

    def save(self,*args,**kwargs):
        if self.date_created is None:
           self.date_created=timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId=str(uuid4()).split('-')[4]
           


        
        self.last_updated=timezone.localtime(timezone.now())
        super(Category,self).save(*args, **kwargs)  

# class Location(models.Model):
#     name = models.CharField(max_length =30, null=True, blank=True)

#     def save_location(self):
#         self.save()

#     def delete_location(self):
#         self.delete()
#     def __str__(self):
#         return self.name

   

class Image(models.Model):
    name = models.CharField(max_length =30)
    descption =models.TextField(null=True,blank=True)
    category= models.ForeignKey(Category, null=True,blank=True,on_delete=models.CASCADE)
    photo =CloudinaryField("photo")
    @classmethod  
    def search_by_category(cls,search_term):
        category = cls.objects.filter(title__icontains=search_term)
        return category 

