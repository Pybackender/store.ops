# Generated by Django 5.1.2 on 2024-11-06 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_image_about_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='title',
            new_name='subject',
        ),
    ]
