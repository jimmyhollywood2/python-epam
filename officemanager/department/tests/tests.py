from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from department.models.models import *

class DepartmentTestCase(TestCase):
    
    def test_str(self):
        """Test string representation of the model"""
        dep = Department(name="New")
        dep.save()
        self.assertEqual(str(dep), dep.name)

class EmployeeTestCase(TestCase):
    
    def test_is_save(self):
        """Test string representation of the model"""
        emp = Employee(
            department=Department.objects.all()[1],
            first_name="Dmitri",
            last_name="Zavadski",
            d_of_b="1995-01-04",
            salary="100000.00"
        )
        emp.save()
        self.assertEqual(str(emp), "Dmitri Zavadski")
