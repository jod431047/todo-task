from django_filters import rest_framework as filters
from .models import Todo


class TodoFilter(filters.FilterSet):
    class Meta:
        model = Todo
        fields ={
            'status': ['exact'],
            'id' : ['range'],
            'name' : ['contains'],
            'description' : ['contains'],
        }