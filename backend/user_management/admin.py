from django.contrib import admin
from .models import TodoUserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class TodoUserProfileInline(admin.StackedInline):
    model = TodoUserProfile

class TodoUserAdmin(UserAdmin):
    inlines = (TodoUserProfileInline, )
    
admin.site.unregister(User)
admin.site.register(User , TodoUserAdmin)