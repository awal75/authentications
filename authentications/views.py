from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserCreateSerializer,ProfileSerilizer
from django.contrib.auth import get_user_model
from .models import Profile
User=get_user_model()

class UserModelViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer

class ProfileModelViewSet(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerilizer