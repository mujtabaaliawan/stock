from rest_framework import serializers
from company.models import Company
from category.serializers import CategorySerializer
from category.models import Category


class CompanySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Company
        fields = '__all__'
