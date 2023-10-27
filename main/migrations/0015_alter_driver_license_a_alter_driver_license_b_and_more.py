# Generated by Django 4.2.5 on 2023-10-18 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_vaccination_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_license',
            name='A',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driver_license',
            name='B',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driver_license',
            name='BE',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driver_license',
            name='C',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driver_license',
            name='CE',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driver_license',
            name='D',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='driver_license',
            name='DE',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='appointment_order_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='appointment_order_num',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='b_day',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='family_status',
            field=models.CharField(blank=True, choices=[('Холост', 'Холост'), ('Женат', 'Женат'), ('В разводе', 'В разводе')], max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='personal_num',
            field=models.CharField(blank=True, max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='place_of_bd',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rank',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.rank'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='second_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='third_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='description',
            field=models.CharField(blank=True, default='-', max_length=50),
        ),
    ]