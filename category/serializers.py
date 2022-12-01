from rest_framework import serializers
from category.models import Category
from company.models import Company
from company.serializers import CompanySerializer


class CategorySerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'company': {'read_only': True}
        }


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'company']

    def update(self, instance, validated_data):
        company = validated_data.get('company')
        instance.company.add(company[0])
        return instance


class EnrollmentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'company']
        