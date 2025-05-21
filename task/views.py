from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from . models import Task, Category, Difficulty
from .serializers import CategorySerializers, TaskSerializers, DifficultySerializers


from django.shortcuts import render


def home(request):
    return render(request, 'tasks/index.html')

def task_list_view(request):
    return render(request, 'tasks/task_list.html')



class CategoryCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()



class DifficultyCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DifficultySerializers
    queryset = Difficulty.objects.all()



class TaskCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers





