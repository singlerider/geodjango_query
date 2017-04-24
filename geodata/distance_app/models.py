# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class GeographyPoint(models.Model):
    # spot_number is the local number associated with a parking spot, not an id
    spot_number = models.PositiveIntegerField()  # no need for negative numbers
    location = models.PointField()


class GeographyPointReservation(models.Model):
    location = models.ForeignKey(
        'GeographyPoint',
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
