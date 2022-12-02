from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from company.models import Company
from favourite.signals import favourite_check
from price.models import Price
from django.core.signals import request_finished


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DataUpdater(APIView):
    parser_classes = [JSONParser]

    def price_update(self, line_data):
        company_name = line_data['company']
        company = Company.objects.get(name=company_name)
        company.price.ldcp = line_data['ldcp']
        company.price.open = line_data['open']
        company.price.high = line_data['high']
        company.price.low = line_data['low']
        company.price.current = line_data['current']
        company.price.change = line_data['change']
        company.price.volume = line_data['volume']

    def create_company(self, line_data):
        ldcp = line_data['ldcp']
        open = line_data['open']
        high = line_data['high']
        low = line_data['low']
        current = line_data['current']
        change = line_data['change']
        volume = line_data['volume']
        new_price = Price.objects.create(ldcp=ldcp, open=open, high=high, low=low,
                                         current=current, change=change, volume=volume)
        new_company = Company.objects.create(name=line_data['company'], price_id=new_price.id)
        market_category = Category.objects.get(name=line_data['category'])
        market_category.company.add(new_company.id)

    def create_category(self, line_data):
        Category.objects.create(name=line_data['category'])
        self.create_company(line_data)

    def post(self, request):
        request_finished.connect(favourite_check)

        market_data = request.data
        for companies in market_data:
            market_category = companies['category']
            market_company = companies['company']
            category_exists = Category.objects.filter(name=market_category).exists()
            company_exists = Company.objects.filter(name=market_company).exists()
            if company_exists:
                self.price_update(companies)
            elif not category_exists:
                self.create_category(companies)
            elif not company_exists:
                self.create_company(companies)
        return JsonResponse("Data Received", safe=False)
