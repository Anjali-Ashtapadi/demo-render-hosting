from rest_framework import serializers
from .models import Todo,Courses

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Courses
    fields = '__all__'