# Generated by Django 2.2.1 on 2019-05-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190524_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_otp_generation',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
