# Generated by Django 5.0.3 on 2024-03-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more', '0017_alter_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Russia'), (2, 'Kazakhstan'), (3, 'Turkmenistan'), (4, 'South Korea'), (5, 'China')], null=True),
        ),
    ]