# Generated by Django 3.1.3 on 2021-02-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_user_pro_membership'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='category',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Investments', 'Investments'), ('Children', 'Children'), ('Other', 'Other')], default='Personal', max_length=11, verbose_name='Category'),
        ),
    ]
