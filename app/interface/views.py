from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request, status
from .models import CustomUser
from .models import Message
from .serializer import UserSerializer
from django.core.exceptions import ValidationError
import telegram
import asyncio
# Create your views here.


async def send_message_by_chat_id(chat_id, message):
    bot = telegram.Bot(token="5855640404:AAFcIc16j9nPjP_j9Df1jJH96e__kHIekBk")
    await bot.send_message(chat_id=chat_id, text=message)


class MessageView(APIView):
    def get(self, requests):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, requests, format=None):
        if requests.data.get("token"):  # connect chat with database
            try:
                user = CustomUser.objects.filter(
                    token=requests.data['token']).exists()
            except ValidationError:
                return Response({"error": "UUID_Validation error"})
            if user:
                user = CustomUser.objects.get(token=requests.data['token'])
            else:
                return Response({"error": "The user is not in the database"})
            user.chat_id = requests.data["chat_id"]
            user.save()

            serializer = UserSerializer(user)
            return Response({"Name": serializer.data})

        if requests.data.get("message") and requests.data.get("login"):
            user = CustomUser.objects.get(
                username=requests.data.get("login"))
            Message.objects.create(user=user, message=requests.data["message"])
            print(user.chat_id)
            asyncio.run(send_message_by_chat_id(
                user.chat_id, requests.data["message"]))
        return Response({"error": "incorrect query"})
