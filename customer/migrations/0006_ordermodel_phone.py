# Generated by Django 3.1.2 on 2021-06-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210604_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
