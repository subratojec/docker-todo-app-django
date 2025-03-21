from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet, index_view, delete_todo, todo_detail

router = DefaultRouter()
router.register(r'todos', TodoItemViewSet, basename='todos')

urlpatterns = [
    path('api/', include(router.urls)),  # API at /api/
    path('', index_view, name='index'),  # UI at /
    path('delete/<uuid:pk>/', delete_todo, name='todo-delete'),  # Delete URL
    path('todo/<uuid:pk>/', todo_detail, name='todo-detail'),  # View URL
]
