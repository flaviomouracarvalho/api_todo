from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets

from app.models import Todo
from app.serializers import TodoSerializers
# Ultilizando viewsets
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

# Class based view automatico pelo rest framework
#class TodoListAndCreate(generics.ListCreateAPIView):
#    queryset = Todo.objects.all()
#    serializer_class = TodoSerializers


#class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Todo.objects.all()
#    serializer_class = TodoSerializers

# Ultilizando o class based view
#class TodoListAndCreate(APIView):
#    def get(self, request):
#        todo = Todo.objects.all()
#        serializer = TodoSerializers(todo, many=True)
#        return Response(serializer.data)
#
#    def post(self, request):
#        serializer = TodoSerializers(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class TodoDetailChangeAndDelete(APIView):
#    def get_object(self, pk):
#        try:
#            return Todo.objects.get(pk=pk)
#        except Todo.DoesNotExist:
#            raise NotFound()
#
#    def get(self, request, pk):
#        serializer = TodoSerializers(self.get_object(pk))
#        return Response(serializer.data)
#
#    def put(self, request, pk):
#        serializer = TodoSerializers(self.get_object(pk), data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
#    def delete(self, request, pk):
#        self.get_object(pk).delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

#Exemplos usando o api_view
#@api_view(['GET', 'POST'])
#def todo_list(request):
#    if request.method == 'GET':
#        todo = Todo.objects.all()
#        serializer = TodoSerializers(todo, many=True)
#        return Response(serializer.data)
#
#    if request.method == 'POST':
#        serializer = TodoSerializers(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#@api_view(['GET', 'PUT', 'DELETE'])
#def todo_detail_change_and_delete(request, pk):
#    try:
#        todo = Todo.objects.get(pk=pk)
#        if request.method == 'GET':
#            serializer = TodoSerializers(todo)
#            return Response(serializer.data)
#
#        if request.method == 'PUT':
#            serializer = TodoSerializers(todo, data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data)
#            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#
#        if request.method == 'DELETE':
#            todo.delete()
#            return Response(status=status.HTTP_204_NO_CONTENT)
#
#    except Todo.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)