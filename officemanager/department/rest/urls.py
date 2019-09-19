from django.urls import path, include
from rest_framework import routers
from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register('department', views.DepartmentViewSet)
ROUTER.register('employee', views.EmployeeViewSet)