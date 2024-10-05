from rest_framework import serializers
from company.models import CompanyDetails

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = '__all__'
