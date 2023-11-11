from django.shortcuts import render
from .models import Todo
from django.views import generic

#def-function for viewjs
def todo_list(request):
    
    return render(request,'todo/vue.html')



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
    
    
class TodoDelete(generic.DeleteView):
    model = Todo
    success_url = '/todo/'
    
    
    