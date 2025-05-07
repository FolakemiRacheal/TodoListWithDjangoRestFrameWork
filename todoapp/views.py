from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.http import JsonResponse
from .serializers import TodoSerializer

@api_view(['GET'])
def restapi(request):
    todoapp_urls ={
        'List':'/todolist/',
        'Detail View':'/todoDetail<str:pk>/',
        'Create' :'/create-todolist/',
        "Update": '/update-todolist/',
        'Delete':"'deleteonetodolist/<str:pk>/"
    }
    return Response(todoapp_urls)

@api_view(["GET"])
def todoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def todoDetail(request, pk):
    todo= Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=True)

    return Response(serializer.data)

@api_view(["POST"])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["PUT"])
def todoUpdate(request, pk):
    todo= Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance = todo, data=request.data)
    return Response(serializer.data)


@api_view(["DELETE"])
def todoDelete(request, pk):
    todo= Todo.objects.get(id=pk)
    todo.delete()
    return Response('Deleted Successfully')


