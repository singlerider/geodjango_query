from ridecell.parking_app.models import ParkingSpot, ParkingSpotReservation, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class ParkingSpotSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ParkingSpot
        fields = ('id', 'latitude', 'longitude', 'spot_number')


class ParkingSpotReservationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ParkingSpotReservation
        fields = (
            'id', 'parking_spot_id', 'user_id',
            'reservation_begin', 'reservation_end'
        )
