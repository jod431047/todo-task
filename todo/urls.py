from django.urls import path
from .views import TodoList,TodoDetail
from todo.api import TodoListAPI 
from todo.api import  TodoDetailAPI
app_name='todo'


urlpatterns = [

    path('todo/api/list',TodoListAPI.as_view()),
    path('todo/api/<int:pk>',TodoDetailAPI.as_view()),
    
    path('todo/', TodoList.as_view()),
    path('todo/<int:pk>', TodoDetail.as_view()),
    
    
   
    
    ]
