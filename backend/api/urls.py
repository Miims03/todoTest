from rest_framework import routers
from .views import TodoViewSet , TodoListViewSet

routers = routers.DefaultRouter()
routers.register('todo', TodoViewSet)
routers.register('todo-list', TodoListViewSet)