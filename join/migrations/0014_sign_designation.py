# Generated by Django 4.1.7 on 2023-08-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0013_rename_signup_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='designation',
            field=models.CharField(choices=[('NGO', 'NGO'), ('Restaurant', 'Restaurant')], default='NGO', max_length=10),
        ),
    ]