from rest_framework import serializers
from price.models import Price
from company.serializers import CompanySerializer
from company.models import Company
from django_filters import rest_framework as filters


class PriceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = Price
        fields = '__all__'


class PriceFilter(filters.FilterSet):
    class Meta:
        model = Price
        fields = {
            'company': ['exact'],
            'date_time': ['lt', 'gt'],
        }
