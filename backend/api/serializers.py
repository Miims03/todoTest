from rest_framework import serializers 

from .models import Todo , TodoList


class TodoSerializer(serializers.ModelSerializer):
    dueDate = serializers.DateField( source='due_date' , format="%d-%m-%Y")
    class Meta:
        model = Todo
        fields = ('id' , 'title', 'dueDate' , 'completed', 'favourited', 'list' )
       
        # exclude = ('due_date',)


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('__all__')
