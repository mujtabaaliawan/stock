from price.models import Price
from price.serializers import PriceSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from company.models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict


class PriceList(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class LatestPriceList(APIView):

    def get(self, request):
        market = dict()
        for company in Company.objects.all():
            price = Price.objects.filter(company=company.id).last()
            market[company.id] = model_to_dict(price)
            market[company.id].update({'company_name': company.name})
            market[company.id].update({'category_id': company.category.id})
            market[company.id].update({'category_name': company.category.name})
        return JsonResponse(market, safe=False)

