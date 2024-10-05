from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from company.models import internshipDetails
from company.Serializers.InternshipSerializers import InternshipDetailsSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

@api_view(['GET'])
@login_required(login_url="/login/")
def internships(request):
    internships = internshipDetails.objects.all()
    serializer = InternshipDetailsSerializer(internships, many=True)
    return render(request, 'internship.html', context={'job_list_all' : serializer.data})
