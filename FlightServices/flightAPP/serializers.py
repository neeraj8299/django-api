import re
from django.db import models
from django.db.models import fields
from rest_framework import serializers, validators
from flightAPP.models import Passenger, Flight, Reservation


def valid(data):
    print(data['flightNumber'])
    return data


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [valid]

    # def validate_flightNumber(self, flightNumber):
    #     if re.match('^[(a-z)]$', flightNumber) == None:
    #         raise serializers.ValidationError('flight number must be valid')
    #     return flightNumber

    def validate(self, attrs):
        print(attrs)
        return attrs


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
