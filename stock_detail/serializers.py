from rest_framework import serializers
from stock_detail.models import StockDetail
from company.serializers import CompanySerializer
from company.models import Company
from django_filters import rest_framework as filters


class StockDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = StockDetail
        fields = '__all__'


class PriceFilter(filters.FilterSet):
    class Meta:
        model = StockDetail
        fields = {
            'company': ['exact'],
            'date_time': ['lt', 'gt'],
        }
