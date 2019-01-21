# Generated by Django 2.1.4 on 2019-01-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='img_logo_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='img_service_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='provides',
            field=models.ManyToManyField(related_name='sensors', to='core.SensorAttribute'),
        ),
        migrations.AlterField(
            model_name='service',
            name='requires',
            field=models.ManyToManyField(related_name='services', to='core.SensorAttribute'),
        ),
    ]