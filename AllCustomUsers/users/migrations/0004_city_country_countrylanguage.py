# Generated by Django 2.2.1 on 2019-05-25 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_last_otp_generation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=52)),
                ('Continent', models.CharField(choices=[('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('Africa', 'Africa'), ('Oceania', 'Oceania'), ('Antarctica', 'Antarctica'), ('South America', 'South America')], default=('Asia', 'Asia'), max_length=20)),
                ('Region', models.CharField(default='', max_length=26)),
                ('SurfaceArea', models.FloatField(default=0.0)),
                ('IndepYear', models.SmallIntegerField(default=None, null=True)),
                ('Population', models.IntegerField(default=0)),
                ('LifeExpectancy', models.FloatField(default=None, null=True)),
                ('GNP', models.FloatField(default=None, null=True)),
                ('GNPOld', models.FloatField(default=None, null=True)),
                ('LocalName', models.CharField(default='', max_length=45)),
                ('GovernmentForm', models.CharField(default='', max_length=45)),
                ('HeadOfState', models.CharField(default=None, max_length=60, null=True)),
                ('Capital', models.IntegerField(default=None, null=True)),
                ('Code2', models.CharField(default='', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('CountryCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.Country')),
                ('Language', models.CharField(default='', max_length=30)),
                ('IsOfficial', models.CharField(choices=[('T', 'T'), ('F', 'F')], default=('F', 'F'), max_length=2)),
                ('Percentage', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=35)),
                ('District', models.CharField(default='', max_length=20)),
                ('Population', models.IntegerField(default=0)),
                ('CountryCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Country')),
            ],
        ),
    ]
