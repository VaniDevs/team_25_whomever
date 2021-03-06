# Generated by Django 2.1.1 on 2018-09-23 19:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_client_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='details',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
