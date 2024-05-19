from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class MeViewSet(viewsets.ViewSet):
    
    permission_classes = (IsAuthenticated, )
    
    @swagger_auto_schema(
        operation_description="Get current user data",
        responses={200: UserSerializer},
        tags=['me']
    )
    
    def list(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)