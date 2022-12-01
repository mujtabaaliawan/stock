from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
