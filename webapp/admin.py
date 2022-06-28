from django.contrib import admin

# Register your models here.
from webapp.models import ToDoList

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'deadline']
    list_display_links = ['title']
    list_filter = ['status']
    search_fields = ['title', 'status']
    fields = ['title', 'status', 'deadline']
    readonly_fields = ['deadline']

admin.site.register(ToDoList, ToDoListAdmin)
