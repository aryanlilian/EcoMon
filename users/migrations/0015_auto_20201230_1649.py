# Generated by Django 3.1.3 on 2020-12-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20201230_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('SLRY', 'Salary'), ('PRFT', 'Profit'), ('INTR', 'Interest'), ('DVDT', 'Divident'), ('RNTL', 'Rental'), ('CPTL', 'Capital'), ('RYLT', 'Royalty'), ('GIFT', 'Gift'), ('OTHR', 'Others')], default='SLRY', max_length=4, verbose_name='Category'),
        ),
    ]
