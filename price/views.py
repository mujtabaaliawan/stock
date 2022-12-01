from price.models import Price
from price.serializers import PriceSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class PriceList(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceCreate(CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceUpdate(RetrieveUpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
