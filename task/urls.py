from django.urls import path
from . import views
from .views import (
    home, task_list_view,
    CategoryCreateAPIView, CategoryRetrieveUpdateDeleteAPIView,
    DifficultyCreateAPIView,
    TaskCreateAPIView, TaskRetrieveUpdateDestroyAPIView,
    TaskFilteredListAPIView
)

urlpatterns = [
    path('api/tasks/', views.TaskFilteredListAPIView.as_view()),
    path('categories/', CategoryCreateAPIView.as_view()),
    path('categories/<int:pk>', CategoryRetrieveUpdateDeleteAPIView.as_view()),
    path('difficulties/', DifficultyCreateAPIView.as_view()),
    path('tasks/', TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('', home, name='index'),
    path('tasks-page/', task_list_view, name='task_list'),
]
