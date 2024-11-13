from django.db import models
from django.core.validators import validate_email
class Contact(models.Model):
    name = models.CharField(null=True,blank=True,max_length=125)
    email = models.EmailField(validators=[validate_email])
    subject = models.CharField(null=True,blank=True,max_length=125)
    message = models.CharField(null=True,blank=True,max_length=335)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name or "Unnamed Contact"

class Title(models.Model):
    title = models.CharField(null=True,blank=True,max_length=205)

    class Meta:
        verbose_name = 'title'
        verbose_name_plural = 'title'

    def __str__(self):
        return self.title