# Generated by Django 4.1.7 on 2023-10-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_relatives_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='speciality',
            field=models.CharField(default='-', max_length=20),
        ),
    ]
