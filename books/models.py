from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)    
    description = models.CharField(max_length=500)   
    url = models.CharField(max_length=255)
    date_added = models.DateField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="books")