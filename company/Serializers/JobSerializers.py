from rest_framework import serializers
from company.models import JobDetails

class JobDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = ['jobId', 'companyId', 'jobDescription', 'qualifications', 'payRange', 'location']
