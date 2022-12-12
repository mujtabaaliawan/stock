from company.models import Company
from company.serializers import CompanySerializer
from rest_framework.generics import ListAPIView


class CompanyList(ListAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


