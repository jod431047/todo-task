from django.urls import path
from .views import TodoList,TodoDetail,TodoCreate,TodoEdit,TodoDelete
from todo.api import  TodoViewsets
from rest_framework.routers import DefaultRouter
from django.urls.conf import include


app_name='todo'
router = DefaultRouter()
router.register('',TodoViewsets)

urlpatterns = [
     
     #html urls
    path('new', TodoCreate.as_view()),
    path('', TodoList.as_view()),
    path('<int:pk>', TodoDetail.as_view()),
    path('<int:pk>/edit', TodoEdit.as_view()),
    path('<int:pk>/delete', TodoDelete.as_view()),
    path('api/', include(router.urls))
    
    ]
