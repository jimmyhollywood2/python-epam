from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=200)

class Employees(models.Model):
    department = models.ForeignKey("departments", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    d_of_b = models.DateField(auto_now=False, auto_now_add=False)
    salary = models.DecimalField( max_digits=9, decimal_places=2)