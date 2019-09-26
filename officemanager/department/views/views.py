from django.shortcuts import render, redirect
from department.models.models import Department, Employee
from department.service import service
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import requests

class DepartmentListView(ListView):

    template_name = 'department.html'
    context_object_name = 'dep_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Department list'
        return context
    
    def get_queryset(self):
        queryset = service.get_departments()
        return queryset
    
class EmployeeListView(ListView):

    template_name = "employee.html"
    context_object_name = 'emp_list'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['title'] = 'Employee list'
        return context
    
    def get_queryset(self):
        queryset = service.get_employees()
        return queryset

def home(request):
    return render(request,'base.html')

def department_by_id(request, pk):
    if request.method == 'GET':
        dep_info = service.get_department_by_id(pk)
        data = {
            'title': dep_info['name'],
            'info': dep_info,
        }
        return render(request, 'department_detail.html', context=data)
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
        return render(request, 'employee_detail.html', context=data)
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
