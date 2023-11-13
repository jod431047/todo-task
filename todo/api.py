
from .serializers import TodoSerializers
from .models import Todo
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from.filters import TodoFilter

class TodoViewsets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    # filterset_fields = ['description', 'name','status']
    
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['description', 'name','status']
    
    
    # filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']
    
    filterset_class =  TodoFilter

