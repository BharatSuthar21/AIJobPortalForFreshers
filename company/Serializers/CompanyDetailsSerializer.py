from rest_framework import serializers
from company.models import companyDetails

class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyDetails
        fields = '__all__'
