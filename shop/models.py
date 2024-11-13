from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['slug']),  # Added index for slug
            models.Index(fields=['title']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Shop(models.Model):
    name = models.CharField(max_length=150)  # Changed to CharField
    slug = models.SlugField(max_length=150, unique=True)  # Added unique=True
    image = models.ImageField(null=True, blank=True, upload_to='shop/%Y/%m/%d')
    price = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    stars = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(null=True,blank=True)
    categories = models.ForeignKey(
        Categories, related_name='shops', on_delete=models.CASCADE)  # Changed related_name
    available = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)  # Indicates if the product is new
    is_on_sale = models.BooleanField(default=False)
   

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Use reverse for consistency
        return reverse('shop:product_detail', args=[self.id, self.slug])
