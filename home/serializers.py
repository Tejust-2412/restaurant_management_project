from rest_framework import serializers 
from .model import MenuCategory 
from .model import MenuItem 



class 


class MenuCategorySerilizer(serializers.ModelSerializer) :
    clas Meta :
    model = MenuCategory
    fields = ['id' , 'name' , 'description', 'price' , 'available' , 'category']

    def validate_price(self , value) :
        if value <= 0 :
            raise serializers.ValidationError('Price must be greater than zero')
        return value