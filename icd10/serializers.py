from icd10.models import Category, ICD
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['code', 'title']


class ICDSerializer(serializers.ModelSerializer):

    class Meta:
        model = ICD
        fields = ['id', 'diagnosis_code', 'full_code', 'abbreviated_description', 'full_description', 'category']
    
    def to_representation(self, instance):
        """Change view of category to include all of its fields in read mode"""
        rep = super().to_representation(instance)
        rep['category']= CategorySerializer(instance.category).data
        return rep

