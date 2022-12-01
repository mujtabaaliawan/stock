from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class TransactionList(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreate(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionUpdate(RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


