from rest_framework import serializers 
from .model import MenuCategory 


class MenuCategorySerilizer(serializers.ModelSerializer) :
    clas Meta :
    model = MenuCategory
    fields = ['id' , 'name']