from rest_framework import serializers
from company.models import internshipDetails

class InternshipDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = internshipDetails
        fields = '__all__'
