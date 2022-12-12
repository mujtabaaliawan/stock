from django.shortcuts import render
from price.models import Price
from company.models import Company
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import datetime
from price.serializers import PriceFilter, PriceSerializer
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
import json


class LatestPriceList(APIView):

    def get(self, request):
        market = dict()
        for company in Company.objects.all():

            price = Price.objects.filter(company=company.id).last()
            company_data = {'category_id': company.category_id, 'category_name': company.category.name,
                            'company_id': company.id, 'company_name': company.name, 'price_id': price.id,
                            'ldcp': price.ldcp, 'open': price.open, 'high': price.high, 'low': price.low,
                            'current': price.current, 'change': price.change, 'volume': price.volume,
                            'date_time': price.date_time
                            }
            market[company.id] = company_data

        return JsonResponse(data=market)


class GraphLogger(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceFilter
