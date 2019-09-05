"""Add model to admin site."""
from django.contrib import admin
from department.models.models import Departments, Employees

admin.site.register(Departments)
admin.site.tegister(Employees)
