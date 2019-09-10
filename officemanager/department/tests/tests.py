from django.test import TestCase
from django.test import Client
from department.models import Department, Employee

class StringReprTestCase(TestCase):
    
    def test_str(self):
        """Testing string representation of the model"""

        dep = Department(name="New")
        dep.save()
        self.assertEqual(str(dep), dep.name)
    
    def test_is_save(self):
        """Testing string representation of the model"""

        emp = Employee(
            department=Department.objects.all()[1],
            first_name="Dmitri",
            last_name="Zavadski",
            d_of_b="1995-01-04",
            salary="100000.00"
        )
        emp.save()
        self.assertEqual(str(emp), "Dmitri Zavadski")

class RESTTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_list(self):
        """View records"""

        resp = self.c.get('/department/list/')
        self.assertEqual(resp.status_code, 200, 'Department list failed')
        resp = self.c.get('/employee/list/')
        self.assertEqual(resp.status_code, 200, 'Employee list failed')
        resp = self.c.get('/employee/detail/2/')
        self.assertEqual(resp.status_code, 200, 'Employee detail failed')
        resp = self.c.get('/department/detail/2/')
        self.assertEqual(resp.status_code, 200, 'Department detail failed')
    
    def test_create_department(self):
        """Create new department"""

        resp = self.c.post('/department/create/', {'name': 'IT department'})
        self.assertEqual(resp.status_code, 201, 'Create department failed')

    def test_create_employee(self):
        """Create new employee"""

        resp = self.c.post('/employee/create/', {
            'department': Department.objects.get(pk=1).pk,
            'first_name': 'Bruce',
            'last_name': 'Willis',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        })
        self.assertEqual(resp.status_code, 201, 'Employee create failed')
    
    def test_put_department(self):
        """Edit record of department table"""

        resp = self.c.put('/department/detail/1/', {'name': 'New It dep'}, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_put_employee(self):
        """Edit record of employee table"""

        emp_data = {
            'department': Department.objects.all()[1].pk,
            'first_name': 'Test',
            'last_name': 'Test',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        }
        resp = self.c.put('/employee/detail/1/', emp_data, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
    
    def test_delete_department(self):
        """Delete record from department table"""

        self.c.delete('/department/detail/1/')
        resp = self.c.get('/department/detail/1/')
        self.assertEqual(resp.status_code, 404)

    def test_delete_employee(self):
        """Delete record from employee table"""
        
        self.c.delete('/employee/detail/1/')
        resp = self.c.get('/employee/detail/1/')
        self.assertEqual(resp.status_code, 404)
