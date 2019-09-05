from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

class Employees(models.Model):
    department = models.ForeignKey("departments", on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    d_of_b = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    salary = models.DecimalField( max_digits=9, decimal_places=2, blank=False, null=False)
