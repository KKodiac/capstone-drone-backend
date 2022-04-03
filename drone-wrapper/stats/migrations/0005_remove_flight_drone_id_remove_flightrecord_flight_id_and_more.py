# Generated by Django 4.0.2 on 2022-03-31 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_rename_end_time_flight_auto_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='drone_id',
        ),
        migrations.RemoveField(
            model_name='flightrecord',
            name='flight_id',
        ),
        migrations.AddField(
            model_name='drone',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.flight'),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.flightrecord'),
        ),
    ]
