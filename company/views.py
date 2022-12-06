from datetime import datetime
from company.models import Company
from company.serializers import CompanySerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.forms.models import model_to_dict
from django.http import JsonResponse
from price.models import Price


class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class GraphLogger(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        from_datetime_value = request.data['from_datetime']
        from_datetime = datetime.strptime(from_datetime_value, '%Y-%m-%d %H:%M:%S')
        to_datetime_value = request.data['to_datetime']
        to_datetime = datetime.strptime(to_datetime_value, '%Y-%m-%d %H:%M:%S')
        company = Company.objects.get(id=request.data['company_id'])
        company_prices = Price.objects.filter(company=company.id, datetime__range=(from_datetime, to_datetime))
        price_values = list(company_prices.values())
        return JsonResponse(price_values, safe=False)





