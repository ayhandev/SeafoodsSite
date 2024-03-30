# Generated by Django 5.0.3 on 2024-03-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more', '0019_alter_product_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[('Russia', 1), ('Kazakhstan', 2), ('Turkmenistan', 3), ('South Korea', 4), ('China', 5)], default=2),
        ),
    ]
