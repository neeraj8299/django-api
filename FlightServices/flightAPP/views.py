from django.shortcuts import render
from flightAPP.models import Flight, Passenger, Reservation
from flightAPP.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['POST'])
def find_flights(request):
    data = Flight.objects.filter(
        departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    data = Flight.objects.get(id=request.data['id'])
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    passenger.save()

    reservation = Reservation()
    reservation.flight = data
    reservation.passenger = passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated)
