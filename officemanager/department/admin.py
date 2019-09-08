"""Add model to admin site."""
from django.contrib import admin
from department.models.models import Department, Employee

admin.site.register(Department)
admin.site.register(Employee)
