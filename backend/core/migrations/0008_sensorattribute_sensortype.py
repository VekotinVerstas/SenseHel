# Generated by Django 2.1.4 on 2019-01-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190115_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorattribute',
            name='sensorType',
            field=models.CharField(default='N/A', max_length=128),
        ),
    ]
