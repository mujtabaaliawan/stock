from price.models import Price
from price.serializers import PriceSerializer
from rest_framework.generics import ListAPIView


class PriceList(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

