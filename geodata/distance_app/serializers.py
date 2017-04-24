from distance_app.models import (
    GeographyPoint, GeographyPointReservation, User)
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name')


class GeographyPointSerializer(serializers.HyperlinkedModelSerializer):
    lat = serializers.SerializerMethodField('latitude')
    lng = serializers.SerializerMethodField('longitude')

    def latitude(self, data):
        return data.location.x

    def longitude(self, data):
        return data.location.y

    class Meta:
        model = GeographyPoint
        fields = ('url', 'id', 'location', 'lat', 'lng', 'spot_number')


class GeographyPointReservationSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.IntegerField()
    geography_point_id = serializers.IntegerField()

    class Meta:
        model = GeographyPointReservation
        fields = (
            'url', 'id', 'geography_point_id', 'user_id',
            'reservation_begin', 'reservation_end'
        )
