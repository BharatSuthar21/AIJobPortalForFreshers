from rest_framework import serializers
from company.models import newsDetails

class NewsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsDetails
        fields = '__all__'
