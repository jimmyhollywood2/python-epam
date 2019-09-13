from django.test import TestCase
from rest_framework.test import APITestCase
from department.models import Department, Employee

class StringReprTestCase(TestCase):
    
    def test_str(self):
        """
        Testing string representation of the model
        """
        dep = Department(name="New")
        dep.save()
        self.assertEqual(str(dep), dep.name)
    
    def test_is_save(self):
        """
        Testing string representation of the model
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

class RESTTestCase(APITestCase):
    def test_list(self):
        """
        View records
        """
        resp = self.client.get('/api/department/')
        self.assertEqual(resp.status_code, 200, 'Department list failed')
        resp = self.client.get('/api/employee/')
        self.assertEqual(resp.status_code, 200, 'Employee list failed')
        resp = self.client.get('/api/employee/2/')
        self.assertEqual(resp.status_code, 200, 'Employee detail failed')
        resp = self.client.get('/api/department/2/')
        self.assertEqual(resp.status_code, 200, 'Department detail failed')
    
    def test_create_department(self):
        """
        Create new department
        """
        resp = self.client.post('/api/department/', {'name': 'IT department'}, format='json')
        self.assertEqual(resp.status_code, 201, 'Create department failed')

    def test_create_employee(self):
        """
        Create new employee
        """
        resp = self.client.post('/api/employee/', {
            'department': Department.objects.get(pk=1).pk,
            'first_name': 'Bruce',
            'last_name': 'Willis',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        })
        self.assertEqual(resp.status_code, 201, 'Employee create failed')
    
    def test_put_department(self):
        """
        Edit record of department table
        """
        resp = self.client.put('/api/department/1/', {'name': 'New It dep'}, format='json')
        self.assertEqual(resp.status_code, 200)
    
    def test_put_employee(self):
        """
        Edit record of employee table
        """
        emp_data = {
            'department': Department.objects.all()[1].pk,
            'first_name': 'Test',
            'last_name': 'Test',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        }
        resp = self.client.put('/api/employee/1/', emp_data, format='json')
        self.assertEqual(resp.status_code, 200)
    
    def test_delete_department(self):
        """
        Delete record from department table
        """
        self.client.delete('/api/department/1/')
        resp = self.client.get('/api/department/1/')
        self.assertEqual(resp.status_code, 404)

    def test_delete_employee(self):
        """
        Delete record from employee table
        """
        self.client.delete('/api/employee/1/')
        resp = self.client.get('/api/employee/1/', format='json')
        self.assertEqual(resp.status_code, 404)
