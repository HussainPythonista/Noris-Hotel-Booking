# Generated by Django 3.1.4 on 2020-12-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20201203_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_type',
            name='roomtype',
            field=models.CharField(choices=[('Lux', 'Luxury'), ('Elt', 'Elite'), ('Sig', 'Signature')], max_length=20),
        ),
    ]
