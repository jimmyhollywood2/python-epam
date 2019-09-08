from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, unique= True, blank=False, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    d_of_b = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False, verbose_name='Date of birth')
    salary = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.department)