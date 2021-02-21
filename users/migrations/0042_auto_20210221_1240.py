# Generated by Django 3.1.3 on 2021-02-21 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20210220_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='users.account'),
        ),
        migrations.AddField(
            model_name='spending',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='spendings', to='users.account'),
        ),
    ]
