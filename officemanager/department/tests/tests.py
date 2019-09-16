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

    def test_department_list(self):
        resp = self.client.get('/api/department/')
        resp_record = resp.json()[0]
        asserted = Department.objects.get(pk=resp_record['id']).name
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['name'], asserted)

    def test_department_by_id(self):
        resp = self.client.get('/api/department/5/')
        resp_record = resp.json()
        asserted = Department.objects.get(pk=5).name
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['name'], asserted)

    def test_employee_list(self):
        resp = self.client.get('/api/employee/')
        resp_record = resp.json()[0]
        asserted = Employee.objects.get(pk=resp_record['id']).first_name
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['first_name'], asserted)

    def test_employee_by_id(self):
        resp = self.client.get('/api/employee/5/')
        resp_record = resp.json()
        asserted = Employee.objects.get(pk=5)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_record['first_name'], asserted.first_name)

    def test_create_department(self):
        """
        Create new department
        """
        data = {
            'name': "IT department",
        }
        resp = self.client.post('/api/department/', data, format='json')
        asserted = Department.objects.get(pk=resp.json()['id'])
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['name'], asserted.name)

    def test_create_employee(self):
        """
        Create new employee
        """
        data = {
            'department': Department.objects.get(pk=1).pk,
            'first_name': 'Bruce',
            'last_name': 'Willis',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        }
        resp = self.client.post('/api/employee/', data, format='json')
        asserted = Employee.objects.get(pk=resp.json()['id'])
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['first_name'], asserted.first_name)
        self.assertEqual(data['last_name'], asserted.last_name)
    
    def test_put_department(self):
        """
        Edit record of department table
        """
        data = {
            'name': 'New name',
        }
        resp = self.client.put('/api/department/1/', data, format='json')
        asserted = Department.objects.get(pk=resp.json()['id'])
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['name'], asserted.name)
    
    def test_put_employee(self):
        """
        Edit record of employee table
        """
        data = {
            'department': Department.objects.all()[1].pk,
            'first_name': 'Test',
            'last_name': 'Test',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        }
        resp = self.client.put('/api/employee/1/', data, format='json')
        asserted = Employee.objects.get(pk=resp.json()['id'])
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['last_name'], asserted.last_name)
    
    def test_delete_department(self):
        """
        Delete record from department table
        """
        Department.objects.create(name="Test")
        added_id = Department.objects.get(name="Test").pk
        self.client.delete('/api/department/{}/'.format(added_id))
        resp = self.client.get('/api/department/{}/'.format(added_id))
        self.assertEqual('Not found.', resp.json()['detail'])

    def test_delete_employee(self):
        """
        Delete record from employee table
        """
        data = {
            'department': Department.objects.all()[4],
            'first_name': 'Test',
            'last_name': 'Test',
            'd_of_b': '1955-03-19',
            'salary': 15000.00
        }
        cr = Employee.objects.create(
            department=data['department'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            d_of_b=data['d_of_b'],
            salary=data['salary'],
        )
        added_id = max([i.id for i in Employee.objects.all()])
        self.client.delete('/api/employee/{}/'.format(added_id))
        resp = self.client.get('/api/employee/{}/'.format(added_id))
        self.assertEqual('Not found.', resp.json()['detail'])
