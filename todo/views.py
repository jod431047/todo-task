from django.shortcuts import render
from models import Todo
from models import generic

# Create your views here.

class TodoList(generic.ListView):
    model = Todo
    
    
class TodoDetail(generic.DetailView):
    model = Todo    
