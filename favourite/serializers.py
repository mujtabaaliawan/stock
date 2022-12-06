from rest_framework import serializers
from favourite.models import Favourite
from company.serializers import CompanySerializer
from company.models import Company
from trader.models import Trader


class FavouriteSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = Favourite
        fields = '__all__'
        extra_kwargs = {
            'trader_user_id': {'read_only': True}
        }

    def create(self, validated_data):
        request = self.context['request']
        new_favourite = Favourite.objects.create(trader_user_id=request.user.id, **validated_data)
        favourite_trader = Trader.objects.get(user_id=request.user.id)
        favourite_trader.favourite.add(new_favourite.id)
        return new_favourite
