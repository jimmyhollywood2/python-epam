from django.test import TestCase
from unittest.mock import patch, Mock
from rest_framework.test import APITestCase
from department.models import Department, Employee
from department.service import service
import json

class StringReprTestCase(TestCase):
    """
    Testing __str__ method
    """
    def test_str_department(self):
        """
        Testing __str__ of Department's model
        """
        dep = Department(name="Test string representation")
        dep.save()
        self.assertEqual(str(dep), "Test string representation")
    
    def test_str_employee(self):
        """
        Testing __str__ of Employee's model
        """
        emp = Employee(
            department=Department.objects.all()[1],
            first_name="Dmitri",
            last_name="Zavadski",
            d_of_b="1995-01-04",
            salary="100000.00"
        )
        emp.save()
        self.assertEqual(str(emp), "Dmitri Zavadski")

class ApiList(APITestCase):
    """
    Testing get method
    """
    def test_department_list(self):
        """
        Get list of departments
        """
        resp = self.client.get('/api/department/')
        resp_record = resp.json()[0]
        asserted = Department.objects.get(pk=resp_record['id']).name
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['name'], asserted)

    def test_department_by_id(self):
        """
        Get department by id
        """
        resp = self.client.get('/api/department/5/')
        resp_record = resp.json()
        asserted = Department.objects.get(pk=5).name
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['name'], asserted)

    def test_employee_list(self):
        """
        Get list of employees
        """
        resp = self.client.get('/api/employee/')
        resp_record = resp.json()[0]
        asserted = Employee.objects.get(pk=resp_record['id']).first_name
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['first_name'], asserted)

    def test_employee_by_id(self):
        """
        Get employee by id
        """
        resp = self.client.get('/api/employee/5/')
        resp_record = resp.json()
        asserted = Employee.objects.get(pk=5)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['first_name'], asserted.first_name)

class ApiCreateDepartment(APITestCase):
    """
    Testing post (create) method of Department
    """
    def setUp(self):
        self.valid_data = {
            'name': 'IT department',
        }
        self.invalid_data = {
            'name': '',
        }
    def test_create_valid_department(self):
        """
        Create new department
        """
        resp = self.client.post('/api/department/', self.valid_data, format='json')
        self.assertEqual(self.valid_data['name'], resp.json()['name'])
    
    def test_create_invalid_department(self):
        """
        Create department with invalid data
        """
        resp = self.client.post('/api/department/', self.invalid_data, format='json')
        self.assertEqual(resp.status_code, 400)

class ApiCreateEmployee(APITestCase):
    """
    Testing post (create) method of employees
    """
    def setUp(self):
        self.valid_data = {
            'department': Department.objects.get(pk=1).pk,
            'first_name': 'Bruce',
            'last_name': 'Willis',
            'd_of_b': '1955-03-19',
            'salary': 15000.00,
        }
        self.invalid_data = {
            'department': Department.objects.get(pk=1).pk,
            'first_name': '',
            'last_name': '',
            'd_of_b': '1955-03-19',
            'salary': 15000.00,
        }

    def test_create_employee(self):
        """
        Create new employee
        """
        resp = self.client.post('/api/employee/', self.valid_data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(self.valid_data['last_name'], resp.json()['last_name'])

    def test_create_invalid_employee(self):
        """
        Create new employee with invalid data
        """
        resp = self.client.post('/api/employee/', self.invalid_data, format='json')
        self.assertEqual(resp.status_code, 400)

class PutDepartment(TestCase):
    """
    Testing post (put) method of department
    """
    def setUp(self):
        self.valid_data = {
            'name': 'New department',
        }
        self.invalid_data = {
            'name': '',
        }
        Department.objects.create(name="New department")
        self.dep_id = Department.objects.get(name="New department").pk

    def test_put_department(self):
        resp = self.client.put(
            '/api/department/{}/'.format(self.dep_id),
            self.valid_data,
            content_type='application/json'
        )
        self.assertEqual(self.valid_data['name'], resp.json()['name'])
    
    def test_put_invalid_department(self):
        """
        Put invalid data 
        """
        resp = self.client.put(
            '/api/department/{}/'.format(self.dep_id),
            self.invalid_data,
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 400)

class PutEmployee(TestCase):
    """
    Testing post (put) method of employee
    """
    def setUp(self):
        self.valid_data = {
            'department': Department.objects.all()[1].pk,
            'first_name': 'Bruce',
            'last_name': 'Willis',
            'd_of_b': '1955-03-19',
            'salary': 15000.00,
        }
        self.invalid_data = {
            'department': Department.objects.all()[1].pk,
            'first_name': '',
            'last_name': '',
            'd_of_b': '1955-03-19',
            'salary': 15000.00,
        }
        Employee.objects.create(
            department=Department.objects.all()[1],
            first_name='Test',
            last_name='Test',
            d_of_b='1900-01-01',
            salary=1000.00,
        )
        self.emp_id = Employee.objects.get(first_name="Test").pk
    
    def test_put_employee(self):
        """
        Edit record of employee table
        """
        resp = self.client.put(
            '/api/employee/{}/'.format(self.emp_id),
            data=json.dumps(self.valid_data),
            content_type='application/json')
        self.assertEqual(self.valid_data['last_name'], resp.json()['last_name'])

    def test_put_invalid_employee(self):
        """
        Edit record of employee table
        """
        resp = self.client.put(
            '/api/employee/{}/'.format(self.emp_id),
            data=json.dumps(self.invalid_data),
            content_type='application/json')
        self.assertEqual(400, resp.status_code)

class DeleteDepartment(TestCase):
    """
    Testing delete method of department
    """
    def setUp(self):
        Department.objects.create(name="ToDelete")
        self.dep_id = Department.objects.get(name='ToDelete').pk
        self.valid_url = '/api/department/{}/'.format(self.dep_id)
        self.invalid_url = '/api/department/{}/'.format(214124)

    def test_delete_department(self):
        resp = self.client.delete(self.valid_url)
        self.assertEqual(204, resp.status_code)

    def test_delete_invalid_url_department(self):
        resp = self.client.delete(self.invalid_url)
        self.assertEqual(404, resp.status_code)

class DeleteEmployee(TestCase):
    """
    Testing delete method of employee
    """
    def setUp(self):
        Employee.objects.create(
            department=Department.objects.all()[1],
            first_name='ToDelete',
            last_name='ToDelete',
            d_of_b='1900-01-01',
            salary=1000.00,
        )
        self.emp_id = Employee.objects.get(first_name="ToDelete").pk
        self.valid_url = '/api/employee/{}/'.format(self.emp_id)
        self.invalid_url = '/api/employee/{}/'.format(214124)

    def test_delete_employee(self):
        resp = self.client.delete(self.valid_url)
        self.assertEqual(204, resp.status_code)
    
    def test_delete_invalid_url_employee(self):
        resp = self.client.delete(self.invalid_url)
        self.assertEqual(404, resp.status_code)

class ServiceDepartments(TestCase):
    @patch('department.service.service')
    def test_get_departments(self, service):
        return_from_mock = sorted([
            'Business Intelligence',
            'IT Management',
            'Administration',
            'IT Procurement',
            'IT Security',
            'Network Adminstration',
            'Systems Analyst & Architecture',
            'User Support & Services',
        ])
        service.get_departments.return_value = return_from_mock
        asserted = sorted([i.name for i in Department.objects.all()])
        resp = service.get_departments()
        self.assertEqual(resp, asserted)
        service.get_departments.assert_called()

class ViewTest(TestCase):
    def test_home_page(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'base.html')
    
    def test_departments(self):
        resp = self.client.get('department/')
        self.assertTemplateUsed(resp, 'department.html')
