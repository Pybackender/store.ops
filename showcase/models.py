from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(null=True, blank=True, max_length=125)
    slug = models.CharField(null=True, blank=True, max_length=125)
    image = models.ImageField(null=True, blank=True,upload_to='Category/%Y/%m/%d')

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField(default=0)
    text = models.TextField()
    available = models.BooleanField(default=True)  # Ensure this line exists

    def get_absolute_url(self):
        return f"/showcase/{self.id}/{self.slug}/"

    def __str__(self):
        return self.name
