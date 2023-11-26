from django.contrib import admin
from .models import ToDoItem

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'due_date', 'created_at', 'completed')
    search_fields = ('title', 'description')