# Generated by Django 3.2.6 on 2021-08-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_blog_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
