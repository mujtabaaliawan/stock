from price.models import Price
from price.serializers import PriceFilter, PriceSerializer
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters


class LatestPriceList(ListAPIView):
    queryset = Price.objects.filter(is_latest=True)
    serializer_class = PriceSerializer


class GraphLogger(ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceFilter
