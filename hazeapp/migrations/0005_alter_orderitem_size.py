# Generated by Django 4.1.6 on 2023-02-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hazeapp', '0004_alter_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=100),
        ),
    ]
