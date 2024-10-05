from rest_framework import serializers
from student.models import studentDashboard

class StudentDashBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentDashboard
        fields = '__all__'
