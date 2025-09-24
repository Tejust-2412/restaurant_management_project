from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIview
from rest_framework import status 
from utils.validation_utils import is_valid_email

# Create your views here.


class EmailCheckView(APIView):
    def post(self , request) :
        email = request.date.get('email')
        if not email :
            return Response({"error " : "Email is required",status = status.HTTP_404_BAD_REQUEST})
            
        if not is_valid_email(email) :
            return Response({"error" :  "Invalid email address"} , status = status.HTTP_404_BAD_REQUEST)

        return Response({"message" : "Email  is valid"} , status= status.HTTP_404_BAD_REQUEST)