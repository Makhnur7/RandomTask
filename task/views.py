from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from django.db.models import Q
import random


from . models import Task, Category, Difficulty
from .serializers import CategorySerializer, TaskSerializer, DifficultySerializer


from django.shortcuts import render


def home(request):
    return render(request, 'tasks/index.html')

def task_list_view(request):
    return render(request, 'tasks/task_list.html')



class CategoryCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class DifficultyCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DifficultySerializer
    queryset = Difficulty.objects.all()



class TaskCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'difficulty']


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

class TaskFilteredListAPIView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.select_related('category', 'difficulty').all()
        category_name = self.request.query_params.get('category')
        difficulty_level = self.request.query_params.get('difficulty')
        randomize = self.request.query_params.get('random')

        if category_name:
            queryset = queryset.filter(category__name=category_name)
        if difficulty_level:
            queryset = queryset.filter(difficulty__level=difficulty_level)
        if randomize == "1":
            queryset = list(queryset)
            random.shuffle(queryset)

        return queryset






