# Generated by Django 3.1.3 on 2020-12-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Income Amount')),
                ('category', models.CharField(choices=[('SLRY', 'Salary'), ('PRFT', 'Profit'), ('ITRT', 'Interest'), ('DVDT', 'Divident'), ('RNTL', 'Rental'), ('CPTL', 'Capital'), ('RYLT', 'Royalty'), ('GIFT', 'Gift'), ('OTRS', 'Others')], default='SLRY', max_length=4, verbose_name='Category')),
                ('recurrent', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Income Amount')),
                ('category', models.CharField(choices=[('UTLT', 'Utilities'), ('RENT', 'Rent'), ('INVC', 'Invoices'), ('SHPG', 'Shopping'), ('FOOD', 'Food'), ('EDCN', 'Education'), ('FUN', 'Fun'), ('INVT', 'Investment'), ('OTRS', 'Others')], default='UTLT', max_length=4, verbose_name='Category')),
                ('recurrent', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
        ),
    ]
