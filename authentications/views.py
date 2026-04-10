from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserCreateSerializer,ProfileSerilizer,ProfileUpdateSerilizer
from django.contrib.auth import get_user_model
from .models import Profile
from rest_framework import permissions
User=get_user_model()

class UserModelViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer
    def get_permissions(self):
        if self.action== 'create':
            return [permissions.AllowAny]
        elif self.action=='list':
            return [permissions.IsAdminUser]
        return [permissions.IsAdminUser]

class ProfileModelViewSet(ModelViewSet):
    queryset=Profile.objects.all()

    def get_serializer_class(self):
        if self.action=='update':
            return ProfileUpdateSerilizer
        return ProfileSerilizer