from django.shortcuts import render
from .models import Todo
from django.views import generic



# Create your views here.

class TodoList(generic.ListView):
    model = Todo
    
    
class TodoDetail(generic.DetailView):
    model = Todo
    
    
class TodoCreate(generic.CreateView):
    model = Todo
    fields = ['name','description','status']
    success_url = '/todo/'
    
    
    
class TodoEdit(generic.UpdateView):
    model = Todo
    fields = ['name','description','status']
    success_url = '/todo/'
    templates_name = 'todo/edit.html'
    
    
    