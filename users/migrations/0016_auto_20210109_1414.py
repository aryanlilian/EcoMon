# Generated by Django 3.1.3 on 2021-01-09 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20201230_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date/Time'),
        ),
    ]
