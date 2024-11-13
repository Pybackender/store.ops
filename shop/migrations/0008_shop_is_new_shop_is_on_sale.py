# Generated by Django 5.1.2 on 2024-11-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shop',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
    ]
