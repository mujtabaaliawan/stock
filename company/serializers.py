from rest_framework import serializers
from company.models import Company
from price.serializers import PriceSerializer
from price.models import Price


class CompanySerializer(serializers.ModelSerializer):
    latest_prices = PriceSerializer(read_only=True)
    latest_prices_id = serializers.PrimaryKeyRelatedField(
        queryset=Price.objects.all(), source='latest_prices', write_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'latest_prices', 'latest_prices_id']


