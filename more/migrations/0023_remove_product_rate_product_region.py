# Generated by Django 5.0.3 on 2024-03-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more', '0022_alter_product_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rate',
        ),
        migrations.AddField(
            model_name='product',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
    ]