from django.db import models

# Create your models here.
class Info(models.Model):
    address = models.CharField(null=True,blank=True,max_length=125)
    locations = models.CharField(null=True,blank=True,max_length=1000)
    phone = models.CharField(null=True,blank=True,max_length=125)
    email = models.CharField(null=True,blank=True,max_length=125)
    instagram = models.CharField(null=True,blank=True,max_length=125)
    youtube = models.CharField(null=True,blank=True,max_length=125)
    linkdin = models.CharField(null=True,blank=True,max_length=125)
    telegram = models.CharField(null=True,blank=True,max_length=125)

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'infos'

    def __str__(self):
        return self.email