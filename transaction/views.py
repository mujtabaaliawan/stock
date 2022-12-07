from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from trader.models import Trader
from django.http import JsonResponse
from transaction.trader_permission import IsTrader


class TransactionCreate(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionList(APIView):

    permission_classes = [IsTrader]

    def get(self, request):

        trader = Trader.objects.get(user_id=request.user.id)
        transactions = Transaction.objects.filter(trader=trader.id)
        transaction_values = list(transactions.values())
        return JsonResponse(transaction_values, safe=False)


