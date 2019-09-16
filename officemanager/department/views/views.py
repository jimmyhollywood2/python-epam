from django.shortcuts import render, redirect
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

def home(request):
    return render(request,'base.html')

def departmentView(request):
    dep_list = service.get_departments()
    data = {
        'title': 'Departments',
        'dep_list': dep_list,
        'add_url': '#',
    }
    return render(request, 'department.html', context=data)

def department_by_id(request, pk):
    if request.method == 'GET':
        dep_info = service.get_department_by_id(pk)
        data = {
            'title': dep_info['name'],
            'info': dep_info,
        }
        return render(request, 'department_info.html', context=data)
    else:
        req_method = request.POST.get('method')

        if req_method == 'delete':
            service.delete_department(request.POST.get('id'))
            return redirect('/department/')

        elif req_method == 'put':
            data = {
                'name': request.POST.get('name')
            }
            service.put_department(pk, data)
            return redirect('/department/')
    
def add_department(request):
    if request.method == 'GET':
        data = {
            'title': 'Add department',
        }
        return render(request, 'add_department.html', context=data)
    else:
        data = {
            'name': request.POST.get('name')
        }
        service.add_department(data)
        return redirect('/department/')

def employeeView(request):
    emp_list = service.get_employees()
    data = {
        'title': 'Employees',
        'emp_list': emp_list,
    }
    return render(request, 'employee.html', context=data)

def employee_by_id(request, pk):
    if request.method == 'GET':
        emp_info = service.get_employee_by_id(pk)
        data = {
            'title': 'Info',
            'info': emp_info,
            'dep_list': Department.objects.all(),
        }
        return render(request, 'employee_info.html', context=data)
    else:
        req_method = request.POST.get('method')
        if req_method == 'delete':
            service.delete_employee(request.POST.get('id'))
            return redirect('/employee/')
        
        elif req_method == 'put':
            data = {
                'department': request.POST.get('department'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'd_of_b': request.POST.get('date_of_birth'),
                'salary': request.POST.get('salary'),
            }
            service.put_employee(pk, data)
            return redirect('/employee/')

def add_employee(request):
    if request.method == 'GET':
        data = {
            'title': 'New employee',
            'dep_list': Department.objects.all(),
        }
        return render(request, 'add_employee.html', context=data)
    else:
        data = {
            'department': request.POST.get('department'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'd_of_b': request.POST.get('date_of_birth'),
            'salary': request.POST.get('salary'),
        }
        service.add_employee(data)
        return redirect('/employee/')
