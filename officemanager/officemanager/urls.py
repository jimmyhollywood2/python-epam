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
from django.urls import path
from department.views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/create/', views.DepartmentCreateView.as_view()),
    path('department/list/', views.DepartmentListView.as_view()),
    path('employee/create/', views.EmployeeCreateView.as_view()),
    path('employee/list/', views.EmployeeListView.as_view()),
    path('employee/detail/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('department/detail/<int:pk>/', views.DepartmentDetailView.as_view()),
]
