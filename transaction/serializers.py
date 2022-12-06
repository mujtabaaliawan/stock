from rest_framework import serializers
from transaction.models import Transaction
from trader.models import Trader
from price.serializers import PriceSerializer
from price.models import Price


class TransactionSerializer(serializers.ModelSerializer):
    price = PriceSerializer(read_only=True)
    price_id = serializers.PrimaryKeyRelatedField(
        queryset=Price.objects.all(), source='price', write_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        transaction_trader = Trader.objects.get(user_id=request.user.id)
        new_transaction = Transaction.objects.create(**validated_data)
        transaction_trader.record.add(new_transaction.id)
        return new_transaction
