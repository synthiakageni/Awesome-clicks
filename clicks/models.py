from enum import unique
from django.db import models
from django.template.defaultfilters import slugify, title
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
from django.urls import reverse
import json
import os

# Create your models here.
class Category(models.Model):
    title = models.CharField(null=True,blank=True,max_length=200)
    uniqueId =models.CharField(null=True,blank=True,max_length=200)
    slug = models.SlugField(max_length=500,unique=True,blank=True,null=True)
    date_created = models.DateTimeField(blank=True,null=True)
    last_updated = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return '{} {}'.format(self.title,self.uniqueId)

    def get_absolute_url(self):
        return reverse('category-detail',kwargs={'slug':self.slug})   

    def save(self,*args,**kwargs):
        if self.date_created is None:
           self.date_created=timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId=str(uuid4()).split('-')[4]
            self.slug=slugify('{}{}'.format(self.title, self.uniqueId))


        self.slug=slugify['{}{}'.format(self.title,self.uniqueId)]
        self.last_updated=timezone.localtime(timezone.now())
        super(Category,self).save(*args, **kwargs)        
