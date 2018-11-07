from rest_framework import routers
from employees.viewsets import EmployeeViewSet, DepartmentViewSet, ProjectViewSet


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'project', ProjectViewSet)
