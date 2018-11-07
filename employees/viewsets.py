from rest_framework import viewsets
from .models import Employee, Department, Project
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer