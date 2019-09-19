from rest_framework import viewsets
from . import serializers
from department.models.models import Department, Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for view and edit Employee
    """
    queryset = Employee.objects.all()
    serializer_class = serializers.EmpoyeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for view and edit Employee
    """
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
