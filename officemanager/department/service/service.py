"""
CRUD operations with DB
"""
import requests
from officemanager.settings import SITE_URL

def get_departments():
    """
    Return list of departments
    """
    url = f"{SITE_URL}/api/department/"
    req = requests.get(url).json()
    return req

def get_department_by_id(id):
    """
    Return info about specified department by id
    """
    url = f"{SITE_URL}/api/department/{id}/"
    req = requests.get(url).json()
    return req

def delete_department(id):
    """
    Delete department by id
    """
    url = f"{SITE_URL}/api/department/{id}/"
    req = requests.delete(url)
    return req

def put_department(id, data):
    """
    Update department
    """
    url = f"{SITE_URL}/api/department/{id}/"
    req = requests.put(url, data)

def add_department(data):
    """
    Create new department
    """
    url = f"{SITE_URL}/api/department/"
    req = requests.post(url, data)

def get_employees():
    """
    Return list of employees
    """
    url = f"{SITE_URL}/api/employee/"
    req = requests.get(url).json()
    return req

def get_employee_by_id(id):
    """
    Return info about specified employee by id
    """
    url = f"{SITE_URL}/api/employee/{id}/"
    req = requests.get(url).json()
    return req

def put_employee(id, data):
    """
    Update employee
    """
    url = f"{SITE_URL}/api/employee/{id}/"
    req = requests.put(url, data)
    
def delete_employee(id):
    """
    Delete employee by id
    """
    url = f"{SITE_URL}/api/employee/{id}/"
    req = requests.delete(url)

def add_employee(data):
    """
    Create new employee
    """
    url = f"{SITE_URL}/api/employee/"
    req = requests.post(url, data)
