# Generated by Django 4.1.7 on 2023-08-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='res',
            name='image',
            field=models.ImageField(upload_to='restaurant_images/'),
        ),
    ]
