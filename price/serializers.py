from rest_framework import serializers
from price.models import Price
from company.serializers import CompanySerializer


class PriceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Price
        fields = '__all__'
