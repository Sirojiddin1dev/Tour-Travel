# Generated by Django 5.0.3 on 2024-04-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='banner_img/')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
    ]