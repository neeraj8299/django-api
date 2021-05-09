from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.

def employeeViews(request):
    emp = {
        'id':1,
        'Name':'Neeraj Kumar',
        'salary':100000,
    }

    data = Employee.objects.all();

    emp = {
        'data':list(data.values())
    }
    return JsonResponse(emp)
