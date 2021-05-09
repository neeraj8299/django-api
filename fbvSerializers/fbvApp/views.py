from django.shortcuts import render
from fbvApp.models import Students
from fbvApp.serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        data = Students.objects.all()
        serializer = StudentsSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    try:
        data = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentsSerializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
