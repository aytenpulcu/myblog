# Generated by Django 3.2.6 on 2021-08-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_blog_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]