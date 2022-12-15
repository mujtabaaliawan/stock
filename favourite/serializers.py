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

    class Meta:
        model = Favourite
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        validated_data['trader'] = Trader.objects.get(user_id=request.user.id)
        return super().create(validated_data)
