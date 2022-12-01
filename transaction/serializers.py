from rest_framework import serializers
from transaction.models import Transaction
from trader.models import Trader
from company.serializers import CompanySerializer
from company.models import Company


class TransactionSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        transaction_trader = Trader.objects.get(user_id=request.user.id)
        new_transaction = Transaction.objects.create(**validated_data)
        transaction_trader.record.add(new_transaction.id)
        return new_transaction
