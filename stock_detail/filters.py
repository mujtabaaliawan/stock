from django_filters import rest_framework as filters
from stock_detail.models import StockDetail


class PriceFilter(filters.FilterSet):
    class Meta:
        model = StockDetail
        fields = {
            'company': ['exact'],
            'date_time': ['lt', 'gt'],
        }
