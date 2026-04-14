from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserCreateSerializer,ProfileSerilizer,ProfileUpdateSerilizer
from django.contrib.auth import get_user_model
from .models import Profile
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .serializers import JwtSerialzer
User=get_user_model()

class UserModelViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserCreateSerializer
    def get_permissions(self):
        if self.action== 'create':
            return [permissions.AllowAny]
        elif self.action=='list':
            return [permissions.IsAdminUser]
        return [permissions.IsAuthenticated]

class ProfileModelViewSet(ModelViewSet):
    queryset=Profile.objects.all()

    def get_serializer_class(self):
        if self.action=='update':
            return ProfileUpdateSerilizer
        return ProfileSerilizer
    

class JwtCreate(CreateAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=JwtSerialzer

    