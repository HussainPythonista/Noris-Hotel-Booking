# Generated by Django 3.1.4 on 2020-12-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20201203_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_type',
            name='roomtype',
            field=models.CharField(choices=[('Lux', 'Luxury'), ('Sig', 'Signature'), ('Elt', 'Elite')], max_length=20),
        ),
    ]
