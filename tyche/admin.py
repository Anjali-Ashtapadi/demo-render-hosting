from django.contrib import admin
from .models import Courses, Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
  list_display = ("task","description","completed")

class CoursesAdmin(admin.ModelAdmin):
  list_display = ("id","course_name","description","duration","tech_stack")

admin.site.register(Todo, TodoAdmin)
admin.site.register(Courses,CoursesAdmin)
