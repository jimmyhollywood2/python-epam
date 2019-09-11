"""
RESTful service implementation
"""

from rest_framework import serializers
from department.models.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    """
    Department's serializer
    """
    average_salary = serializers.SerializerMethodField('get_average_salary')

    def get_average_salary(self, obj):
        salary = [i.salary for i in Employee.objects.filter(department_id=obj.id)]
        if len(salary) != 0:
            return round(sum(salary) / (len(salary)), 2)
        return 0

    class Meta:
        model = Department
        fields = ('id', 'name', 'average_salary')

class EmpoyeeSerializer(serializers.ModelSerializer):
    """
    Eployee's serializer
    """
    class Meta:
        model = Employee
        fields = ('id', 'department', 'first_name', 'last_name', 'd_of_b', 'salary')

    def to_representation(self, instance):
        rep = super(EmpoyeeSerializer, self).to_representation(instance)
        rep['department'] = instance.department.name
        return rep
