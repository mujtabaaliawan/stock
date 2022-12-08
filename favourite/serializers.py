from rest_framework import serializers
from favourite.models import Favourite
from company.serializers import CompanySerializer
from trader.serializers import TraderSerializer
from company.models import Company
from trader.models import Trader


class FavouriteSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)
    trader = TraderSerializer(read_only=True)
    trader_id = serializers.PrimaryKeyRelatedField(
        queryset=Trader.objects.all(), source='trader', write_only=True)

    class Meta:
        model = Favourite
        fields = '__all__'
