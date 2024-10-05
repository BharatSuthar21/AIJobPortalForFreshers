from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from company.models import JobDetails
from company.Serializers.JobSerializers import JobDetailsSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required(login_url="/login/")
@api_view(['GET'])
def jobs(request):
    jobs = JobDetails.objects.all()
    serializer = JobDetailsSerializer(jobs, many=True)
    return render(request, 'job.html', context={'job_list_all' : serializer.data})
