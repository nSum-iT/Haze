# Generated by Django 4.1.6 on 2023-02-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hazeapp', '0007_remove_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
