from django.shortcuts import render
from rest_framework import viewsets
from department.rest import rest
from department.models.models import Department, Employee

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for view and edit Employee
    """
    queryset = Employee.objects.all()
    serializer_class = rest.EmpoyeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for view and edit Employee
    """
    queryset = Department.objects.all()
    serializer_class = rest.DepartmentSerializer
