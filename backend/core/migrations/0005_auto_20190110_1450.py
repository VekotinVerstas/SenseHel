# Generated by Django 2.1.4 on 2019-01-10 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190109_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentSensorValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apartment_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ApartmentSensor')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.SensorAttribute')),
            ],
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='sensors',
        ),
        migrations.AddField(
            model_name='apartmentsensor',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='core.Apartment'),
        ),
        migrations.AddField(
            model_name='apartmentsensor',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Sensor'),
        ),
    ]
