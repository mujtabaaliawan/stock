from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.generics import ListCreateAPIView


class TransactionCreate(ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        current_user_id = self.request.user.id
        return Transaction.objects.filter(trader__user_id=current_user_id)



