import requests
#CRUD operations with DB

def get_departments():
    """
    Return list of departments
    """
    url = "http://127.0.0.1:8000/api/department/"
    req = requests.get(url).json()
    return req

def get_employees():
    """
    Return list of employees
    """
    url = "http://127.0.0.1:8000/api/employee/"
    req = requests.get(url).json()
    return req

def get_department_by_id(id):
    """
    Return info about specified department by id
    """
    url = "http://127.0.0.1:8000/api/department/{}/".format(id)
    req = requests.get(url).json()
    return req

def get_employee_by_id(id):
    """
    Return info about specified employee by id
    """
    url = "http://127.0.0.1:8000/api/employee/{}/".format(id)
    req = requests.get(url).json()
    return req

def delete_department(id):
    url = "http://127.0.0.1:8000/api/department/{}/".format(id)
    req = requests.delete(url)

def put_department(id, data):
    url = "http://127.0.0.1:8000/api/department/{}/".format(id)
    req = requests.put(url, data)