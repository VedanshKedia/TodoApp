from django.contrib import admin
from .models import TodoListItem
# Register your models here.

# admin.site.register(TodoListItem)


@admin.register(TodoListItem)
class TodoListItemAdmin(admin.ModelAdmin):
    list_display = ('todoTitle', 'todoDescription', 'todoDateTime', 'priority', 'status')
