from django.contrib import admin

from contact.models import Contact, Title

# Register your models here.
@admin.register(Contact)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject']
    
admin.site.register(Title)