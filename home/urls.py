from django.urls import path
from .views import *

urlpatterns = [
    path ('categories/' , MenuCategoryListview.as_view() , name='menu-categories'),
    
]