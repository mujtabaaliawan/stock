from company.models import Company
from company.serializers import CompanySerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreate(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdate(RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


