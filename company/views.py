from datetime import datetime
from company.models import Company
from company.serializers import CompanySerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
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

        category_id = company.category.id
        category_name = company.category.name
        company_id = company.id
        company_name = company.name
        company_data = dict()
        company_data['category_id'] = category_id
        company_data['category_name'] = category_name
        company_data['company_id'] = company_id
        company_data['company_name'] = company_name

        price_data = list(company_prices.values())

        graph_data = [company_data, price_data]

        return JsonResponse(graph_data, safe=False)





