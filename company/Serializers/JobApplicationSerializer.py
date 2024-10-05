from rest_framework import serializers
from company.models import jobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobApplication
        fields = '__all__'
