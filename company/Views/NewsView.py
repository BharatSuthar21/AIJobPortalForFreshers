from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from company.models import newsDetails
from company.Serializers.NewsSerializers import NewsDetailsSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


@login_required(login_url="/login/")
@api_view(['GET'])
def news(request):
    news = newsDetails.objects.all()
    serializer = NewsDetailsSerializer(news, many=True)
    return render(request, 'news.html', context={'news_list_all' : serializer.data})