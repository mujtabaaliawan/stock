from trader.models import Trader
from trader.serializers import TraderSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class TraderList(ListAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer


class TraderCreate(CreateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer


class TraderUpdate(RetrieveUpdateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

