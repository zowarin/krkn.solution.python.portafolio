# Generated by Django 2.2.7 on 2019-12-20 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20191220_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaboradorcliente',
            options={'ordering': ['actualidad', '-fecha_inicio', '-fecha_fin']},
        ),
    ]
