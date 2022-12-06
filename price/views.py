from price.models import Price
from price.serializers import PriceSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from company.models import Company
from django.http import JsonResponse


class PriceList(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class LatestPriceList(APIView):

    def get(self, request):
        market = []
        for company in Company.objects.all():
            company_data = dict()
            price = Price.objects.filter(company=company.id).last()

            company_data['category_id'] = company.category.id
            company_data['category_name'] = company.category.name
            company_data['company_id'] = company.id
            company_data['company_name'] = company.name
            company_data['ldcp'] = price.ldcp
            company_data['open'] = price.open
            company_data['high'] = price.high
            company_data['low'] = price.low
            company_data['current'] = price.current
            company_data['change'] = price.change
            company_data['volume'] = price.volume

            market.append(company_data)

        return JsonResponse(market, safe=False)

