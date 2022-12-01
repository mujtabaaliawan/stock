from category.models import Category
from category.serializers import CategorySerializer, EnrollmentSerializer, EnrollmentUpdateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Enrollment(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = EnrollmentUpdateSerializer




