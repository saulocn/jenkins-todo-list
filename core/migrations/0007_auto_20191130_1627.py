# Generated by Django 2.1.7 on 2019-11-30 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191130_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 11, 30, 16, 27, 6, 674649)),
        ),
    ]
