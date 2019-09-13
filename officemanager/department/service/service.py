import requests
#CRUD operations with DB

def get_departments():
    url = "http://127.0.0.1:8000/api/department/"
    req = requests.get(url).json()
    return req

def get_employees():
    url = "http://127.0.0.1:8000/api/employee/"
    req = requests.get(url).json()
    return req

def get_department_by_id(num):
    url = "http://127.0.0.1:8000/api/department/{}/".format(num)
    req = requests.get(url).json()
    return req

def get_employee_by_id(num):
    url = "http://127.0.0.1:8000/api/employee/{}/".format(num)
    req = requests.get(url).json()
    return req