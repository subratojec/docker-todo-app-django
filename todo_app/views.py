# todo_app/views.py
import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import DestroyModelMixin
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.viewsets import GenericViewSet, ViewSet


LOGGER = logging.getLogger(__name__)
class TodoItemViewSet(GenericViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    
    # Custom create method
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            LOGGER.error(e,exc_info=True)
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Custom destroy method
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        LOGGER.info(f"Deleted task {instance.title}")
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Custom update method
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
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

    # Custom get method
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
