# Generated by Django 4.0.2 on 2022-04-07 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_rename_admin_id_drone_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='deck',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.deck'),
        ),
        migrations.AlterField(
            model_name='drone',
            name='drone_alias',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='drone',
            name='flight',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.flight'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_path',
            field=models.JSONField(null=True),
        ),
    ]
