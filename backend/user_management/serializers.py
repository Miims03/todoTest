
from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import TodoUserProfile


class TodoUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUserProfile
        fields = ('phone', )

class UserSerializer(serializers.ModelSerializer):
    profile = TodoUserProfileSerializer(source = 'todouserprofile')
    class Meta:
        model = User
        fields = ("id" , "username" , "email" , "profile" )