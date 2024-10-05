from rest_framework import serializers
from company.models import jobDetails

class JobDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobDetails
        fields = '__all__'
