# Generated by Django 2.2.1 on 2019-05-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_successful_auth',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp_random',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
