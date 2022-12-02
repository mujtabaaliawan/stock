from manager.models import Manager
from manager.serializers import ManagerSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class ManagerList(ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerCreate(CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerUpdate(RetrieveUpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

