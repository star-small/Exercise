from rest_framework import routers
from django.urls import path
from .api import UserViewSet
from .views import MessageView
router = routers.DefaultRouter()
router.register("api/user", UserViewSet, "user")

urlpatterns = [
    path("api/user/", MessageView.as_view())
]
