from django.db import models


class Employee(models.Model):
    emp_number = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    dept_name = models.CharField(max_length=250)
    project_name = models.CharField(max_length=250)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Employee {self.first_name} {self.second_name} ({self.dept_name} of {self.project_name})'

