# Generated by Django 3.1.5 on 2021-01-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=60, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(blank=True, max_length=30, verbose_name='marital status'),
        ),
    ]