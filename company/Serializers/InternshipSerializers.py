from rest_framework import serializers
from company.models import InternshipDetails

class InternshipDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipDetails
        fields = ['internshipId', 'companyId', 'internshipDescription', 'qualifications', 'payRange', 'location']
