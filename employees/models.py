from django.db import models


class Employee(models.Model):
    emp_number = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    department = models.ForeignKey('Department', related_name='members', on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Employee {self.first_name} {self.second_name}'


class Department(models.Model):
    name = models.CharField(max_length=250)
    manager = models.ForeignKey('Employee', related_name="managed_departments", on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey('Project', related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Department {self.name} of project {self.project.name}'


class Project(models.Model):
    name = models.CharField(max_length=250)
    manager = models.ForeignKey('Employee', related_name="managed_projects", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Project {self.name}'
