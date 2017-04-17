# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('spot_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpotReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_begin', models.DateTimeField()),
                ('reservation_end', models.DateTimeField()),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.ParkingSpot')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='parkingspotreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_app.User'),
        ),
    ]