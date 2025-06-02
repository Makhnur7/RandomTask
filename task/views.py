from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter
from django.db.models import Q
import random

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import *
from .serializers import *
from .forms import *
from .utils import DataMixin



def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    
    return render(request, 'task/index.html', {'form': form})

                    
def home(request):
    return render(request, 'tasks/index.html')

def task_list_view(request):
    return render(request, 'tasks/task_list.html')

def registration_view(request):
    return render(request, 'tasks/registration_list.html')






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

def task_dashboard(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_dashboard')  

    return render(request, 'tasks/dashboard.html', {
        'form': form,
        'tasks': tasks
    })

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_dashboard')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('task_dashboard')




class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tasks/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('task_dashboard')


def logout_user(request):
    logout(request)
    return redirect('login')



