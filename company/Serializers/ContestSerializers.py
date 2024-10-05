from rest_framework import serializers
from company.models import ContestDetails

class ContestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestDetails
        fields = '__all__'
