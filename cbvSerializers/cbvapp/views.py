from django.shortcuts import render
from cbvapp.models import Students
from cbvapp.serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.


class StudentPagination(PageNumberPagination):
    page_size = 2


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'score']
    ordering = ['-name']


"""
# genric uses


class StudentList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
# mixins Uses


class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

# class view
"""class StudentList(APIView):

    def get(self, request):
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):

    def get_object(self, pk):
        try:
            data = Students.objects.get(pk=pk)
            return data
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = StudentsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = StudentsSerializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
