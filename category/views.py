from category.models import Category
from category.serializers import CategorySerializer, EnrollmentSerializer, EnrollmentUpdateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


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


class DataUpdater(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        new_data = request.data
        print(request.data)
        return JsonResponse("Data Received", safe=False)



