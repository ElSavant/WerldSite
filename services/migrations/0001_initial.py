# Generated by Django 3.1 on 2021-07-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='service_images/')),
                ('short_descr', models.TextField(max_length=200)),
                ('long_descr', models.TextField(max_length=5000)),
            ],
        ),
    ]
