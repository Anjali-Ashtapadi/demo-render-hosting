from django.urls import path,include
from .views import CoursesView
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'tasks',TodoView, basename='task')
router.register(r'courses',CoursesView, basename='course')
urlpatterns=[
  path('api/',include(router.urls)),
  # path('about/',about),
  # path('contact/',contact)
]