from trader.models import Trader
from rest_framework import serializers
from user.serializers import UserSerializer


class TraderSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Trader
        fields = ['id', 'user', 'role', 'mobile_number', 'record', 'favourite']
        extra_kwargs = {
            'record': {'read_only': True},
            'favourite': {'read_only': True}
        }

    def create(self, validated_data):
        user = UserSerializer.create(self, validated_data=validated_data)
        role = validated_data.get('role')
        mobile_number = validated_data.get('mobile_number')
        trader, created = Trader.objects.update_or_create(user=user, role=role, mobile_number=mobile_number)
        return trader


