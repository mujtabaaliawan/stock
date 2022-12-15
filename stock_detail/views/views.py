from stock_detail.models import StockDetail
from stock_detail.serializers import StockDetailSerializer
from stock_detail.filters import PriceFilter
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters


class StockDetailList(ListAPIView):
    queryset = StockDetail.objects.filter(is_latest=True)
    serializer_class = StockDetailSerializer


class GraphLogger(ListAPIView):
    queryset = StockDetail.objects.all()
    serializer_class = StockDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PriceFilter
