from django.urls import path
from . import views

from .views import home,task_list_view


urlpatterns = [
    path('categories/', views.CategoryCreateAPIView.as_view()),
    path('categories/<int:pk>', views.CategoryRetrieveUpdateDeleteAPIView.as_view()),
    path('difficulties/', views.DifficultyCreateAPIView.as_view()),
    path('tasks/', views.TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('', home, name='index'),
    path('tasks-page/', task_list_view, name='task_list'),
]
