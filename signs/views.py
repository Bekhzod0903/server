from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CategorySerializer, RoadSignsSerializer
from .models import Category, RoadSigns

# Create your views here.

class ListCategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        serializer_data = {
            'categories': serializer.data,
            'count': categories.count(),
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data, status=status.HTTP_404_NOT_FOUND)
