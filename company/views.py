from datetime import datetime
from company.models import Company
from company.serializers import CompanySerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.forms.models import model_to_dict
from django.http import JsonResponse


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
        prices_data = dict()
        i = 1
        for value in company.price.all():
            current_datetime = value.datetime
            if from_datetime < current_datetime < to_datetime:
                prices_data[i] = model_to_dict(value)
                i = i+1
        return JsonResponse(prices_data, safe=False)



