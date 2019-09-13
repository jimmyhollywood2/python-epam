from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework import viewsets
from department.rest import rest
from department.models.models import Department, Employee
from department.service import service

#API

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for view and edit Employee
    """
    queryset = Employee.objects.all()
    serializer_class = rest.EmpoyeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for view and edit Employee
    """
    queryset = Department.objects.all()
    serializer_class = rest.DepartmentSerializer

#HTML

def departmentView(request):
    dep_list = service.get_departments()
    data = {
        'title': 'Departments',
        'dep_list': dep_list,
    }
    return render(request, 'department.html', context=data)

def employeeView(request):
    emp_list = service.get_employees()
    data = {
        'title': 'Emplpoyees',
        'emp_list': emp_list,
    }
    return render(request, 'employee.html', context=data)

def department_by_id(request, pk):
    dep_info = service.get_department_by_id(pk)
    data = {
        'title': 'Info',
        'info': dep_info,
    }
    return render(request, 'department_info.html', context=data)

def employee_by_id(request, pk):
    emp_info = service.get_employee_by_id(pk)
    data = {
        'title': 'Info',
        'info': emp_info,
    }
    return render(request, 'employee_info.html', context=data)
