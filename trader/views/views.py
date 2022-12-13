from trader.models import Trader
from trader.serializers import TraderSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class TraderList(ListCreateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer


class TraderUpdate(RetrieveUpdateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

