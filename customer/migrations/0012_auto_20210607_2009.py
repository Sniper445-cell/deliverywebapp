# Generated by Django 3.1.2 on 2021-06-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20210607_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
