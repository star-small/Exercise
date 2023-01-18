from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    first_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} - {self.token}"


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        CustomUser, related_name="messages", on_delete=models.CASCADE)
