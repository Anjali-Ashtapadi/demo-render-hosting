from django.db import models

# Create your models here.
class Courses(models.Model):
  course_name = models.CharField(max_length =100)
  description = models.CharField(max_length=250)
  duration = models.CharField(max_length = 100)
  tech_stack = models.CharField(max_length = 250)

  def __str__(self):
    return self.course_name
  
  class Meta:
    verbose_name_plural = "Courses"

class Todo(models.Model):
  task = models.CharField(max_length = 150)
  description = models.CharField(max_length= 250)
  completed = models.BooleanField(default = False)

  def __str__(self):
    return self.task

  