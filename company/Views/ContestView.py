from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from company.models import contestDetails
from company.Serializers.ContestSerializers import ContestDetailsSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required(login_url="/login/")
@api_view(['GET'])
def contests(request):
    news = contestDetails.objects.all()
    serializer = ContestDetailsSerializer(news, many=True)
    return render(request, 'contest.html', context={'contest_list_all' : serializer.data})