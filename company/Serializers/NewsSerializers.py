from rest_framework import serializers
from company.models import NewsDetails

class NewsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetails
        fields = '__all__'
