from rest_framework.decorators import api_view
from rest_framework.response import Response
from company.models import CompanyDetails
from company.Serializers.CompanyDetailsSerializer import CompanyDetailsSerializer

@api_view(['GET', 'POST'])
def manage_company(request):
    if request.method == 'GET':
        companies = CompanyDetails.objects.all()
        serializer = CompanyDetailsSerializer(companies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompanyDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
