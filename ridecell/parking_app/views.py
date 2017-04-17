# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ridecell.parking_app.models import (ParkingSpot, ParkingSpotReservation,
                                         User)
from rest_framework import viewsets
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
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer


class ParkingSpotReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ParkingSpotReservation.objects.all()
    serializer_class = ParkingSpotReservationSerializer
