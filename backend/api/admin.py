from django.contrib import admin
from .models import Todo, TodoList

# Register your models here.

class ToodoInLine(admin.TabularInline):
    model = Todo
    extra = 0

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ToodoInLine]
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'favourited')
    list_filter = ('due_date', 'completed', 'favourited')
    search_fields = ('title','completed','favourited')
    pass