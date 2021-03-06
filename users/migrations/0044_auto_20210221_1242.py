# Generated by Django 3.1.3 on 2021-02-21 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20210221_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='users.account'),
        ),
        migrations.AlterField(
            model_name='spending',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spendings', to='users.account'),
        ),
    ]
