from trader.models import Manager
from trader.serializers import ManagerSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class TraderList(ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class TraderCreate(CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class TraderUpdate(RetrieveUpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

