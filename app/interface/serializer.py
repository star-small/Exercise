from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    message_user = serializers.RelatedField(source='message', read_only=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "message_user")
