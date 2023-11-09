from django.urls import path
from .views import TodoList,TodoDetail,TodoCreate,TodoEdit,TodoDelete
from todo.api import TodoListAPI 
from todo.api import  TodoDetailAPI


app_name='todo'


urlpatterns = [
     #urls api
    path('todo/api/list',TodoListAPI.as_view()),
    path('todo/api/<int:pk>',TodoDetailAPI.as_view()),
    
     
     #html urls
    path('new', TodoCreate.as_view()),
    path('', TodoList.as_view()),
    path('<int:pk>', TodoDetail.as_view()),
    path('<int:pk>/edit', TodoEdit.as_view()),
    path('<int:pk>/delete', TodoDelete.as_view()),
   
    
    ]
