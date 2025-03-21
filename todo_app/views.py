import logging
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.viewsets import GenericViewSet

LOGGER = logging.getLogger(__name__)

# View to render the index.html template with the list of todos
def index_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            TodoItem.objects.create(title=title)
        return redirect('index')  # Redirect to the same page after adding
    todos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': todos})

# View to delete a todo item
def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('index')
    return redirect('index')

# View to view a single todo item (optional, for the "View" link)
def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

# Existing API ViewSet
class TodoItemViewSet(GenericViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            LOGGER.error(e, exc_info=True)
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        LOGGER.info(f"Deleted task {instance.title}")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            LOGGER.error(e)
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            LOGGER.error(e)
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):  # Renamed 'get' to 'retrieve' to match DRF convention
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
