"""
CRUD operations with DB
"""
import requests

def get_departments():
    """
    Return list of departments
    """
    url = "http://127.0.0.1:8000/api/department/"
    req = requests.get(url).json()
    return req

def get_department_by_id(id):
    """
    Return info about specified department by id
    """
    url = "http://127.0.0.1:8000/api/department/{}/".format(id)
    req = requests.get(url).json()
    return req

def delete_department(id):
    """
    Delete department by id
    """
    url = "http://127.0.0.1:8000/api/department/{}/".format(id)
    req = requests.delete(url)

def put_department(id, data):
    """
    Update department
    """
    url = "http://127.0.0.1:8000/api/department/{}/".format(id)
    req = requests.put(url, data)

def add_department(data):
    """
    Create new department
    """
    url = "http://127.0.0.1:8000/api/department/"
    req = requests.post(url, data)

def get_employees():
    """
    Return list of employees
    """
    url = "http://127.0.0.1:8000/api/employee/"
    req = requests.get(url).json()
    return req

def get_employee_by_id(id):
    """
    Return info about specified employee by id
    """
    url = "http://127.0.0.1:8000/api/employee/{}/".format(id)
    req = requests.get(url).json()
    return req

def put_employee(id, data):
    """
    Update employee
    """
    url = "http://127.0.0.1:8000/api/employee/{}/".format(id)
    req = requests.put(url, data)
    
def delete_employee(id):
    """
    Delete employee by id
    """
    url = "http://127.0.0.1:8000/api/employee/{}/".format(id)
    req = requests.delete(url)

def add_employee(data):
    """
    Create new employee
    """
    url = "http://127.0.0.1:8000/api/employee/"
    req = requests.post(url, data)
