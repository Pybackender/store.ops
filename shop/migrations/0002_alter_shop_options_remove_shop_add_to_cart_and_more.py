# Generated by Django 5.1.2 on 2024-11-07 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Shop', 'verbose_name_plural': 'Shops'},
        ),
        migrations.RemoveField(
            model_name='shop',
            name='add_to_cart',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='is_on_sale',
        ),
    ]
