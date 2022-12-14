# Generated by Django 4.1.1 on 2022-09-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banner/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Banner',
            },
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'Setting'},
        ),
    ]
