from django.db import models
from django.db.models import fields
from rest_framework import serializers
from fbvApp.models import Passenger, Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['firstName', 'lastName', 'travelEndPoint']
