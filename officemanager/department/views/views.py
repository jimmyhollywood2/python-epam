from django.shortcuts import render
from rest_framework import generics
from department.rest import rest
from department.models import models
# Create your views here.

class DepartmentCreateView(generics.CreateAPIView):
    """API view for create new record in department table"""
    serializer_class = rest.DepartmentSerializer

class DepartmentListView(generics.ListAPIView):
    """API view for show all records from department table"""
    queryset = models.Department.objects.all()
    serializer_class = rest.DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show detail from only one record"""
    queryset = models.Department.objects.all()
    serializer_class = rest.DepartmentSerializer

class EmployeeCreateView(generics.CreateAPIView):
    """API view for create new record in employee table"""
    serializer_class = rest.EmpoyeeSerializer

class EmployeeListView(generics.ListAPIView):
    """API view for show all records from employee table"""
    queryset = models.Employee.objects.all()
    serializer_class = rest.EmpoyeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show detail from only one record"""
    queryset = models.Employee.objects.all()
    serializer_class = rest.EmpoyeeSerializer
