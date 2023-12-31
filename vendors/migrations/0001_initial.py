# Generated by Django 5.0 on 2023-12-05 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vender_code', models.CharField(max_length=150)),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfilment_rate', models.FloatField()),
            ],
            options={
                'verbose_name': 'vendor',
                'verbose_name_plural': 'vendors',
                'db_table': 'vendors_vendor',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Perfomance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_date', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_respose_time', models.FloatField()),
                ('fulfilment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor')),
            ],
            options={
                'verbose_name': 'perfomance',
                'verbose_name_plural': 'perfomances',
                'db_table': 'vendors_perfomance',
                'ordering': ('-id',),
            },
        ),
    ]
