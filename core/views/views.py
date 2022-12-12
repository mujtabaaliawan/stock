from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from category.models import Category
from company.models import Company
from favourite.signals import favourite_check
from price.serializers import PriceSerializer
from django.core.signals import request_finished
from core.authentications.sender_authentication import SenderAuthentication
from rest_framework.permissions import IsAuthenticated
from price.models import Price


class DataUpdater(APIView):

    parser_classes = [JSONParser]
    authentication_classes = [SenderAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        request_finished.connect(favourite_check)
        Price.objects.filter(is_latest=True).update(is_latest=False)
        for companies in request.data:

            category, created = Category.objects.get_or_create(name=companies['category'])
            company, created = Company.objects.get_or_create(name=companies['company'],
                                                             defaults={'category_id': category.id})
            companies['company_id'] = company.id
            companies['category_id'] = category.id
            companies['is_latest'] = True

            serializer = PriceSerializer(data=companies)
            serializer.is_valid()
            serializer.save()

        return JsonResponse("Data Received", safe=False)
