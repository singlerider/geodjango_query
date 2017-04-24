# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from distance_app.models import GeographyPoint, GeographyPointReservation, User
from distance_app.serializers import (GeographyPointReservationSerializer,
                                      GeographyPointSerializer, UserSerializer)
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GeographyPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows geography points to be viewed or edited.
    """
    queryset = GeographyPoint.objects.all()
    serializer_class = GeographyPointSerializer

    def _get_available_spots(self, predefined_spots=None):
        now = datetime.now()
        if not predefined_spots:
            reservations = GeographyPointReservation.objects.filter(
                reservation_begin__lt=now,
                reservation_end__gte=now
            )
            excluded_ids = tuple([x.geography_point_id for x in reservations])
            spots = GeographyPoint.objects.exclude(id__in=excluded_ids)
            return spots
        else:
            included_ids = tuple([x.id for x in predefined_spots])
            reservations = GeographyPointReservation.objects.filter(
                reservation_begin__lt=now,
                reservation_end__gte=now
            )
            reservations = reservations.filter(
                id__in=included_ids
            )
            excluded_ids = tuple([x.geography_point_id for x in reservations])
            filtered_spots = GeographyPoint.objects.exclude(
                id__in=excluded_ids
            )
            filtered_spots = filtered_spots.filter(
                id__in=included_ids
            )
            return list(filtered_spots)

    def _get_spots_in_range(
            self, latitude, longitude, radius, radius_in_miles=True):
        if radius_in_miles:
            radius = radius * 1609.34
        results = GeographyPoint.objects.filter(location__distance_lt=(
            Point(latitude, longitude), Distance(km=radius)))
        return list(results)

    def get_queryset(self):
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)
        radius = self.request.query_params.get('radius', None)
        if latitude and longitude and radius is not None:
            spots_in_range = self._get_spots_in_range(
                latitude, longitude, radius
            )
            available_spots = self._get_available_spots(
                predefined_spots=spots_in_range)
            return available_spots
        else:
            results = self._get_available_spots()
            return results


class GeographyPointReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows geography point reservations to be viewed or edited.
    """
    queryset = GeographyPointReservation.objects.all()
    serializer_class = GeographyPointReservationSerializer
