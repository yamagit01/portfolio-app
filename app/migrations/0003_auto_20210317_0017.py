# Generated by Django 3.1.7 on 2021-03-16 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Work',
            old_name='images',
            new_name='image'
        )
    ]
