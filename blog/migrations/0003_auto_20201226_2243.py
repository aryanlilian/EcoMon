# Generated by Django 3.1.3 on 2020-12-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201217_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('FAMILY', 'Family'), ('BUSSINESS', 'Bussiness'), ('MARKETING', 'Marketing'), ('SPENDINGS', 'Spendings')], default='BUSSINESS', max_length=9, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Title'),
        ),
    ]
