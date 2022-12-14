# Generated by Django 3.2.6 on 2021-08-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='url',
            new_name='content',
        ),
        migrations.AddField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='sidebar',
            field=models.BooleanField(default=True),
        ),
    ]
