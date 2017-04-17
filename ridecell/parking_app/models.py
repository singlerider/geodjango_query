# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class ParkingSpot(models.Model):
    latitude = models.FloatField(  # I'd implement DecimalField with more time
        default=0.0
    )
    longitude = models.FloatField(  # I'd implement DecimalField with more time
        default=0.0
    )
    # spot_number is the local number associated with a parking spot, not an id
    spot_number = models.PositiveIntegerField()  # no need for negative numbers


class ParkingSpotReservation(models.Model):
    parking_spot = models.ForeignKey(
        'ParkingSpot',
        models.CASCADE,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        'User',
        models.CASCADE,
        blank=False,
        null=False,
    )
    reservation_begin = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=False, null=False
    )
    reservation_end = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=False, null=False
    )
