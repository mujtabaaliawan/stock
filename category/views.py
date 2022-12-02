from category.models import Category
from category.serializers import CategorySerializer, EnrollmentSerializer, EnrollmentUpdateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from company.models import Company
from price.models import Price
from favourite.models import Favourite
from django.core.mail import send_mail
from trader.models import Trader


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Enrollment(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = EnrollmentUpdateSerializer


class DataUpdater(APIView):
    parser_classes = [JSONParser]

    def favourite_check(self):
        favourites = Favourite.objects.all()
        print("Yes i am working")
        for fav in favourites:
            field = fav.price_field
            company_current_price = fav.company.price.objects.get(field)
            if company_current_price <= fav.minimum_limit:
                favourite_trader = Trader.objects.get(user_id=fav.trader_user_id)
                email = favourite_trader.user.email
                send_mail(
                    'Market Favourite Company Price Alert',
                    f'Favourite Company {fav.company} has reached minimum limit, new value is {company_current_price}',
                    'mujtaba.ali@ignicube.com',
                    [email],
                )
            if company_current_price >= fav.maximum_limit:
                favourite_trader = Trader.objects.get(user_id=fav.trader_user_id)
                email = favourite_trader.user.email
                send_mail(
                    'Market Favourite Company Price Alert',
                    f'Favourite Company {fav.company} has reached maximum limit, new value is {company_current_price}',
                    'mujtaba.ali@ignicube.com',
                    [email],
                )

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
        market_data = request.data
        data = market_data[0]
        print(type(data), data['category'])

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

        self.favourite_check()
        return JsonResponse("Data Received", safe=False)





