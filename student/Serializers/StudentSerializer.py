from rest_framework import serializers
from student.models import studentDetails

class studentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentDetails
        fields = '__all__'
