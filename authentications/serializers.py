from rest_framework import serializers
import models
from django.conf import settings
from django.db import transaction
from django.contrib.auth import get_user_model

User=User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        with transaction.atomic():
            # 1. Extract profile data
            first_name = validated_data.pop('first_name')
            last_name = validated_data.pop('last_name')

            # 2. Create the User first (using the manager to hash password)
            user = User.objects.create_user(**validated_data)

            # 3. Create the Profile linked to the new User
            models.Profile.objects.create(
                user=user, 
                first_name=first_name, 
                last_name=last_name
            )

            return user
        
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email']
    
class ProfileSerilizer(serializers.ModelSerializer):
    user=SimpleUserSerializer(read_only=True)
    class Meta:
        model=models.Profile
        fields=['id','user','first_name','last_name','phone','date_of_birth','bio','profile_picture','address','city','country','is_verified','created_at','updated_at']


class ProfileUpdateSerilizer(serializers.ModelSerializer):
    class Meta:
        model=models.Profile
        fields=['id','first_name','last_name','phone','date_of_birth','bio','profile_picture','address','city','country','is_verified','created_at','updated_at']


