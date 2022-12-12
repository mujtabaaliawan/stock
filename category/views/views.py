from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.generics import ListAPIView


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

