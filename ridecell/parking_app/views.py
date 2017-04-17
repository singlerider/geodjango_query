# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from ridecell.parking_app.models import (ParkingSpot, ParkingSpotReservation,
                                         User)
from ridecell.parking_app.serializers import (ParkingSpotReservationSerializer,
                                              ParkingSpotSerializer,
                                              UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parking spots to be viewed or edited.
    """
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)
        radius = self.request.query_params.get('radius', None)
        if latitude and longitude:
            if radius:
                return self.queryset  # TODO: actually filter on radius
            else:  # search for a spot based on exact location
                return ParkingSpot.objects.filter(
                    latitude=latitude, longitude=longitude
                )
        else:
            return self.queryset


class ParkingSpotReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parking spot reservations to be viewed or edited.
    """
    queryset = ParkingSpotReservation.objects.all()
    serializer_class = ParkingSpotReservationSerializer
