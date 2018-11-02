from rest_framework import routers
from employees.viewsets import EmployeeViewSet


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
