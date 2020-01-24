# Generated by Django 3.0.2 on 2020-01-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('countryCode1', models.CharField(max_length=4)),
                ('mobileNumber1', models.IntegerField()),
                ('countryCode2', models.CharField(max_length=4)),
                ('mobileNumber2', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('website', models.URLField()),
            ],
        ),
    ]
