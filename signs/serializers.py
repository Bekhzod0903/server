from rest_framework import serializers
from .models import Category, RoadSigns

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    class Meta:
        model = Category
        fields = '__all__'


class RoadSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSigns
        fields = '__all__'

