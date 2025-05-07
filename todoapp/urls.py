from django.urls import path
from . import views

urlpatterns = [
    path('', views.restapi, name="restapi_page"),
    path('todolist/', views.todoList, name='todo_list'),
    path('todoDetail/<str:pk>/', views.todoDetail, name='todo_Detail'),
    path('update-todolist/<str:pk>/', views.todoUpdate, name='todo_Update'),
    path('create-todolist/', views.todoCreate, name='create_todolist'),
    path('deleteonetodolist/<str:pk>/', views.todoDelete, name='delete_one_todolist'),
]