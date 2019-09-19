"""officemanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from department.views import views
from department.rest.urls import ROUTER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/', include(ROUTER.urls)),
    path('department/', views.DepartmentListView.as_view()),
    path('employee/', views.EmployeeListView.as_view()),
    path('department/<int:pk>/', views.department_by_id),
    path('employee/<int:pk>/', views.employee_by_id),
    path('department/add/', views.add_department),
    path('employee/add/', views.add_employee),
]
