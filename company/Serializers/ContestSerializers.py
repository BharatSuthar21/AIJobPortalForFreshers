from rest_framework import serializers
from company.models import contestDetails

class ContestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contestDetails
        fields = '__all__'
