from rest_framework import serializers
from .models import Employee, Department, Project



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=False, allow_null=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        try:
            dpt = Department.objects.get(pk=validated_data.pop('department').get('id'))
        except (KeyError, AttributeError):
            dpt = None

        emp = Employee.objects.create(department=dpt, **validated_data)
        return emp

    def update(self, instance, validated_data):
        try:
            dpt = Department.objects.get(pk=validated_data.pop('department').get('id'))
        except (KeyError, AttributeError):
            dpt = None

        for k, v in validated_data.items():
            setattr(instance, k, v)

        instance.department = dpt
        instance.save()
        return instance
