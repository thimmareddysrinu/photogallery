# Generated by Django 4.2.5 on 2023-09-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_remove_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
