# Generated by Django 5.0.3 on 2024-03-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more', '0014_remove_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(default="{static 'images/cel.png'}", upload_to='media/'),
        ),
    ]
