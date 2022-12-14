from rest_framework import serializers
from transaction.models import Transaction
from trader.models import Trader
from trader.serializers import TraderSerializer
from stock_detail.serializers import StockDetailSerializer
from stock_detail.models import StockDetail


class TransactionSerializer(serializers.ModelSerializer):
    stock_detail = StockDetailSerializer(read_only=True)
    stock_detail_id = serializers.PrimaryKeyRelatedField(
        queryset=StockDetail.objects.all(), source='stock_detail', write_only=True)
    trader = TraderSerializer(read_only=True)
    trader_id = serializers.PrimaryKeyRelatedField(
        queryset=Trader.objects.all(), source='trader', write_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        request = self.context['request']
        trader = data.get('trader')
        trader_validate = trader.user.id == request.user.id
        volume_transacted = data.get('volume_transacted')
        stock_data = data.get('stock_detail')
        company = stock_data.company
        volume_current = stock_data.volume

        nature = data.get('nature')

        if all([trader_validate, nature == 'purchase', volume_transacted <= volume_current]):
            return data

        elif all([trader_validate, nature == 'sale']):

            transactions_data = Transaction.objects.filter(trader=trader, stock_detail__company=company)

            volume_available = 0
            for transaction in transactions_data:
                if transaction.nature == "purchase":
                    volume_available = volume_available + transaction.volume_transacted
                else:
                    volume_available = volume_available - transaction.volume_transacted

            if volume_transacted <= volume_available:
                return data

        raise serializers.ValidationError("Invalid Transaction")
