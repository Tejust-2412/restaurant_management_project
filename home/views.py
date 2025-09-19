from django.shortcuts import render
from rest_framework.generics import ListAPIview 
from .models import MenuCategory
from .serializers import MenuCategorySerializer

# Create your views here.

class MenuCategoryListView(ListAPIView) :
    queryset = MenuCategory.object.all()
    serializer_clas = MenuCategorySerializer