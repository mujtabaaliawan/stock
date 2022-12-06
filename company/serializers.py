from rest_framework import serializers
from company.models import Company
from category.serializers import CategorySerializer


class CompanySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


