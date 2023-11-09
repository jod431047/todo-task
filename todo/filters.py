from django_filters import rest_framework as filters
from .models import Todo


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Todo
        fields ={
            'status': ['exact'],
        }