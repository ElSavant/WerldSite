# Generated by Django 3.1 on 2021-07-05 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='long_descr',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='short_descr',
            new_name='short_description',
        ),
    ]
