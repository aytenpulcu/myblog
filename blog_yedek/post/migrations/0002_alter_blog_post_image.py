# Generated by Django 3.2.6 on 2021-08-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(upload_to='post'),
        ),
    ]
