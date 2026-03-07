from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer


User=get_user_model()

class UserModelViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer
