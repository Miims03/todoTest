from django.shortcuts import render
from rest_framework import viewsets , generics
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import filters
from django.http import HttpRequest , JsonResponse , HttpResponse 

from .models import Todo , TodoList
from .serializers import TodoSerializer , TodoListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from http import HTTPStatus

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter ,DjangoFilterBackend ,)
    filterset_fields = ('due_date', 'completed', 'favourited' )
    search_fields = ('title', )

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )
    
    
def helloWorld(request: HttpRequest, name):
    
    if request.user.is_anonymous:
        return HttpResponse(status=HTTPStatus.FORBIDDEN)
    
    if request.method == 'GET':
        return JsonResponse({'message': f'Hello {name}!'})
    else:
        return HttpResponse(status=HTTPStatus.METHOD_NOT_ALLOWED)
    