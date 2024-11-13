from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(null=True,blank=True,max_length=125)
    subject = models.CharField(null=True,blank=True,max_length=125)
    image = models.ImageField(null=True,blank=True)
    text = models.CharField(null=True,blank=True,max_length=125)

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'homes'

    def __str__(self):
        return self.title