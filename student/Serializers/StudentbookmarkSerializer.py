from rest_framework import serializers
from student.models import studentBookmark

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentBookmark
        fields = '__all__'
