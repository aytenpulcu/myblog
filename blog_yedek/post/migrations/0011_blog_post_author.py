# Generated by Django 3.2.6 on 2021-08-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='author',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]