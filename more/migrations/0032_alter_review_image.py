# Generated by Django 5.0.3 on 2024-04-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more', '0031_visitcounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, default='cel.png', upload_to='images/'),
        ),
    ]
