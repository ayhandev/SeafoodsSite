# Generated by Django 5.0.3 on 2024-03-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more', '0012_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=1000),
        ),
    ]
