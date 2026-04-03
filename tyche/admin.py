from django.contrib import admin
from .models import Courses, Todo
# Register your models here.

admin.site.register(Courses)

class TodoAdmin(admin.ModelAdmin):
  list_display = ("task","description","completed")

admin.site.register(Todo, TodoAdmin)