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
from category.sender_authentication import SenderAuthentication
from rest_framework.permissions import IsAuthenticated


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DataUpdater(APIView):

    parser_classes = [JSONParser]
    authentication_classes = [SenderAuthentication]
    permission_classes = [IsAuthenticated]

    def price_update(self, line_data):

        ldcp = line_data['ldcp']
        open = line_data['open']
        high = line_data['high']
        low = line_data['low']
        current = line_data['current']
        change = line_data['change']
        volume = line_data['volume']
        date_time = line_data['date_time']
        company_name = line_data['company']
        company = Company.objects.get(name=company_name)
        Price.objects.create(company=company, ldcp=ldcp, open=open, high=high, low=low,
                             current=current, change=change, volume=volume, date_time=date_time)

    def create_company(self, line_data):

        category = Category.objects.get(name=line_data['category'])
        Company.objects.create(name=line_data['company'], category=category)
        self.price_update(line_data)

    def create_category(self, line_data):

        Category.objects.create(name=line_data['category'])
        self.create_company(line_data)

    def post(self, request):

        request_finished.connect(favourite_check)

        for companies in request.data:
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
