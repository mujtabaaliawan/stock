from rest_framework import serializers
from company.models import Company
from price.serializers import PriceSerializer
from price.models import Price


class CompanySerializer(serializers.ModelSerializer):
    price = PriceSerializer(read_only=True)
    price_id = serializers.PrimaryKeyRelatedField(
        queryset=Price.objects.all(), source='price', write_only=True)

    class Meta:
        model = Company
        fields = '__all__'


        