from django.db import models


class Checkout(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True,blank=True)
    different_address = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_names = models.TextField(blank=True, null=True)  
    quantities = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "checkout"
        verbose_name_plural = "checkouts"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
