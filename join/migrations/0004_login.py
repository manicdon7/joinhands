# Generated by Django 4.1.7 on 2023-08-21 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_res_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
