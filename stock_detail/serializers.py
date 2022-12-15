from rest_framework import serializers
from stock_detail.models import StockDetail
from company.serializers import CompanySerializer
from company.models import Company


class StockDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = StockDetail
        fields = '__all__'
