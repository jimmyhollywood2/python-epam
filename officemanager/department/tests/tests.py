from django.test import TestCase, RequestFactory
from unittest.mock import patch, Mock
from rest_framework.test import APITestCase
from department.models import Department, Employee
from department.service import service
from department.views.views import DepartmentListView,EmployeeListView
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

class ViewTest(TestCase):
    def test_home_page(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'base.html')
    
    @patch('department.service.service.get_department_by_id')
    def test_department_by_id(self, patch_get_department_by_id):
        patch_get_department_by_id.return_value = {
            'id': 99,
            'name': 'Name 1',
            'average_salary': 10000.00
        }
        resp = self.client.get('/department/99/')
        self.assertTemplateUsed(resp, 'department_detail.html')
        self.assertEqual(resp.status_code, 200)
    
    @patch('department.service.service.get_employee_by_id')
    def test_employee_by_id(self, patch_get_employee_by_id):
        patch_get_employee_by_id.return_value = {
            'id': 1000,
            'department': 'Department',
            'first_name': 'Name 1',
            'last_name': 'Last name',
            'salary': 10000.00,            
        }
        resp = self.client.get('/employee/1000/')
        self.assertTemplateUsed(resp, 'employee_detail.html')
        self.assertEqual(resp.status_code, 200)
    
    @patch('department.service.service.get_departments')
    def test_get_departments(self, patch_get_departments):
        patch_get_departments.return_value = [
            {"id":3,"name":"Administration","average_salary":11986.41},
            {"id":1,"name":"Business Intelligence","average_salary":11898.22},
            {"id":2,"name":"IT Management","average_salary":8598.29}
        ]
        resp = self.client.get('/department/')
        self.assertTemplateUsed(resp, 'department.html')
        self.assertEqual(resp.status_code, 200)
    
    @patch('department.service.service.get_employees')
    def test_get_employees(self, patch_get_employees):
        patch_get_employees.return_value = [
            {"id":1,
            "department":"User Support & Services",
            "first_name":"Dmitri",
            "last_name":"Hyneman",
            "d_of_b":"1964-07-08",
            "salary":"6486.77"
            },
            {"id":2,
            "department":"IT Management",
            "first_name":"Nina",
            "last_name":"Stepaniuk",
            "d_of_b":"1959-04-01",
            "salary":"2359.33"
            },
            {"id":3,"department":"User Support & Services",
            "first_name":"Krisitna",
            "last_name":"McFly",
            "d_of_b":"1981-02-28",
            "salary":"17092.36"
            },
            {"id":4,
            "department":"IT Management",
            "first_name":"Alexandra",
            "last_name":"Kluni",
            "d_of_b":"1979-12-13",
            "salary":"7934.22"
            },
            {"id":5,
            "department":"IT Security",
            "first_name":"Kirill",
            "last_name":"Savage",
            "d_of_b":"1954-05-17",
            "salary":"2213.78"
            }
        ]
        resp = self.client.get('/employee/')
        self.assertTemplateUsed(resp, 'employee.html')
        self.assertEqual(resp.status_code, 200)

    @patch('department.service.service.add_department')
    def test_add_dertment(self, patch_add_department):
        patch_add_department.return_value = 204
        resp = self.client.get('/department/add/')
        self.assertTemplateUsed(resp, 'add_department.html')
        self.assertEqual(resp.status_code, 200)

    @patch('department.service.service.add_employee')
    def test_add_employee(self, patch_add_employee):
        patch_add_employee.return_value = 204
        resp = self.client.get('/employee/add/')
        self.assertTemplateUsed(resp, 'add_employee.html')
        self.assertEqual(resp.status_code, 200)

class TestClassBasedViews(TestCase):
    @patch('department.views.views.DepartmentListView.get_queryset')
    def test_department_list_view(self, get_queryset):
        get_queryset.return_value = [
            {'id':1,
            'name':'name',
            'average_salary':10000},
            {'id':2,
            'name':'name2',
            'average_salary':10000},
            {'id':3,
            'name':'name3',
            'average_salary':10000},
        ]
        request = RequestFactory().get('/department/')
        view = DepartmentListView.as_view()
        resp = view(request)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.template_name[0], 'department.html')
        self.assertEqual(resp.context_data['object_list'][0],{'id':1,'name':'name','average_salary':10000})

    @patch('department.views.views.EmployeeListView.get_queryset')
    def test_employee_list_view(self, get_queryset):
        get_queryset.return_value = [
            {"id":1,
            "department":"User Support & Services",
            "first_name":"Dmitri",
            "last_name":"Hyneman",
            "d_of_b":"1964-07-08",
            "salary":"6486.77"
            },
        ]
        request = RequestFactory().get('/employee/')
        view = EmployeeListView.as_view()
        resp = view(request)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.template_name[0], 'employee.html')
    
class ServiceTest(TestCase):
    def test_get_department(self):
        request = RequestFactory().get('/department/')
        view = DepartmentListView.as_view()
        resp = view(request)
        service_res = service.get_departments()
        self.assertEqual(service_res, resp.context_data['object_list'])

    def test_get_employee(self):
        request = RequestFactory().get('/employee/')
        view = EmployeeListView.as_view()
        resp = view(request)
        service_res = service.get_employees()
        self.assertEqual(service_res, resp.context_data['object_list'])
