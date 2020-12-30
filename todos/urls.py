from django.urls import path
from . import views

urlpatterns = [
    path('', views.todosOverview, name="todos-overview"),
    path('todo-list/', views.todoList, name="todo-list"),
    path('todo-detail/<int:id>/', views.todoDetail, name="todo-detail"),
    path('todo-create/', views.todoCreate, name="todo-create"),
    path('todo-update/<int:id>/', views.todoUpdate, name="todo-update"),
    path('todo-delete/<int:id>/', views.todoDelete, name="todo-delete"),
]