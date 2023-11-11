
from .serializers import TodoSerializers
from .models import Todo


from rest_framework import viewsets


class TodoViewsets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    
    

