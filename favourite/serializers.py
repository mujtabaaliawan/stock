from rest_framework import serializers
from favourite.models import Favourite
from company.serializers import CompanySerializer
from company.models import Company


class FavouriteSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = Favourite
        fields = ['id', 'company', 'price_field', 'minimum_limit', 'maximum_limit', 'company_id', 'trader_user_id']
        extra_kwargs = {
            'trader_user_id': {'read_only': True}
        }

    def create(self, validated_data):
        request = self.context['request']
        new_favourite = Favourite.objects.create(trader_user_id=request.user.id, **validated_data)
        return new_favourite
