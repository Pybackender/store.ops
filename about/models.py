from django.db import models

# Create your models here.


class About(models.Model):
    text = models.CharField(null=True, blank=True, max_length=125)
    subject = models.CharField(null=True, blank=True, max_length=125)
    image = models.ImageField(null=True, blank=True,
                              upload_to='about/%Y/%m/%d')

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'

    def __str__(self):
        return self.text


class Service(models.Model):
    title = models.CharField(null=True, blank=True, max_length=125)
    icon = models.CharField(null=True, blank=True, max_length=125)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Brands(models.Model):
    image = models.ImageField(null=True, blank=True,
                              upload_to='brand/%Y/%m/%d')
    link = models.URLField(null=True,blank=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

