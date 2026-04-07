from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses
from .serializers import  CoursesSerializer
from rest_framework import viewsets
# Create your views here.
# def homepage(request):
#   return HttpResponse("Welcome to Tyche, the library management system!")

# def about(request):
#   return HttpResponse("This is the about page of Tyche.")

# def contact(request):
#   email = 'tyche@gmail.com'
#   address = 'Idukki, Kerala'
#   contact_numbers = ['9846543210', '9876543210']
#   logged_in_status = True
#   personal_data = {'Business_Type':'Education','Location':'Idukki','Established':'2025'}
#   age = 18
#   return render(request,'contact.html',{'emailid':email,'address_data':address,'contact_numbers':contact_numbers,'logged_status':logged_in_status,'age':age,'data':personal_data})

# class TodoView(viewsets.ModelViewSet):
#   serializer_class = TodoSerializer
#   queryset = Todo.objects.all()


class CoursesView(viewsets.ModelViewSet):
  serializer_class = CoursesSerializer
  queryset = Courses.objects.all()