# Generated by Django 2.2.7 on 2019-12-05 01:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20191204_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='fecha_nac',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
