from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import UserSerializer


# Create your views here.

class MessageView(APIView):
    def get(self, requests):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, requests, format=None):
        user = CustomUser.objects.get(token=requests.data['token'])
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response({"wrefer": "wfwef"})
