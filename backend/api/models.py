from django.db import models
from private_storage.fields import PrivateFileField 

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    favourited = models.BooleanField(default=False)
    attachments = models.FileField(upload_to='public', null=True)
    private_file = PrivateFileField(upload_to='private', null=True)

    list = models.ForeignKey('TodoList', on_delete=models.CASCADE, null=False)

    # def __str__(self):
    #     return self.title

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Todo Lists'
        verbose_name = 'Todo List'