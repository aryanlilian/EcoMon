# Generated by Django 3.1.3 on 2021-02-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210206_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='full_image',
            field=models.ImageField(default='blog_pics/full_blog_image.jpg', upload_to='blog_pics', verbose_name='Full Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='medium_image',
            field=models.ImageField(default='blog_pics/medium_blog_image.jpg', upload_to='blog_pics', verbose_name='Medium Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='small_image',
            field=models.ImageField(default='blog_pics/small_blog_image.jpg', upload_to='blog_pics', verbose_name='Small Image'),
        ),
    ]
