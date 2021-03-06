# Generated by Django 3.1 on 2021-07-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='team_images/')),
                ('role', models.CharField(max_length=200)),
                ('short_description', models.TextField(max_length=200)),
                ('long_description', models.TextField(max_length=5000)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
    ]
