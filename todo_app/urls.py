# todo_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet
from todo_project import settings

router = DefaultRouter()
router.register(r'todos', TodoItemViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls)),
]
