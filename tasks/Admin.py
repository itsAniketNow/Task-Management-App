from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')  # Show these fields in the list view
    search_fields = ('title', 'description')  # Add search functionality
    list_filter = ('user',)  # Add filter options by user
