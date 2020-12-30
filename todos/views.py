from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

@api_view(['GET'])
def todosOverview(request):
  todos_urls = {
    'List': '/todo-list',
    'Detail view' : '/todo-detail/<int:id>',
    'Create': '/todo-create/',
    'Update': '/todo-update/<int:id>',
    'Delete': '/todo-delete/<int:id>',
  }
  return Response(todos_urls)

@api_view(['GET'])
def todoList(request):
  todos = Todo.objects.all()
  serializer =  TodoSerializer(todos, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, id):
  todo = Todo.objects.get(id=id)
  serializer =  TodoSerializer(todo, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
  serializer =  TodoSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, id):
  todo = Todo.objects.get(id=id)
  serializer =  TodoSerializer(instance=todo, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, id):
  todo = Todo.objects.get(id=id)
  todo.delete()

  return Response({
    "message": "Todo of id:" + str(id) + " deleted",
    "id": id
  })
