from rest_framework import serializers
from company.models import companyDashboard

class DashBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyDashboard
        fields = '__all__'
