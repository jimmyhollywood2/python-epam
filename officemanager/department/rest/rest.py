"""RESTful service implementation"""

from rest_framework import serializers
from department.models.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    """Configure department's serializer"""
    class Meta:
        model = Department
        fields = '__all__'

class EmpoyeeSerializer(serializers.ModelSerializer):
    """Configure employee's serializer"""
    department = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = '__all__'

