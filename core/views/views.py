from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from category.models import Category
from company.models import Company
from favourite.signals import favourite_check
from stock_detail.serializers import StockDetailSerializer
from django.core.signals import request_finished
from core.authentications.sender_authentication import SenderAuthentication
from rest_framework.permissions import IsAuthenticated
from stock_detail.models import StockDetail


class DataUpdater(APIView):

    parser_classes = [JSONParser]
    authentication_classes = [SenderAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        request_finished.connect(favourite_check)
        StockDetail.objects.filter(is_latest=True).update(is_latest=False)
        for company_data in request.data:

            category, created = Category.objects.get_or_create(name=company_data['category'])
            company, created = Company.objects.get_or_create(name=company_data['company'],
                                                             defaults={'category_id': category.id})
            company_data['company_id'] = company.id
            company_data['category_id'] = category.id
            company_data['is_latest'] = True

            serializer = StockDetailSerializer(data=company_data)
            serializer.is_valid()
            serializer.save()

        return JsonResponse("Data Received", safe=False)
