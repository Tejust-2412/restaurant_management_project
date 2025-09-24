from django.shortcuts import render
from rest_framework.generics import ListAPIview 
from .models import MenuCategory
from .serializers import MenuCategorySerializer

# Create your views here.

class MenuCategoryListView(ListAPIView) :
    queryset = MenuCategory.object.all()
    serializer_clas = MenuCategorySerializer


    def get_quertset(self) :
        queryset = MenuItem.objects.all()
        query = self.request.query_params.get('q')

        if query :
            queryset = query.filter(name_icontains = query)

        return queryset.order_by ('name')

