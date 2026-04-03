from django.urls import path,include
from .views import homepage,about,contact,TodoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks',TodoView, basename='task')

urlpatterns=[
  path('',homepage),
  path('api/',include(router.urls)),
  path('about/',about),
  path('contact/',contact)
]