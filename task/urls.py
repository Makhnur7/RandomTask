from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('api/tasks/', views.TaskFilteredListAPIView.as_view()),
    path('categories/', CategoryCreateAPIView.as_view()),
    path('categories/<int:pk>', CategoryRetrieveUpdateDeleteAPIView.as_view()),
    path('difficulties/', DifficultyCreateAPIView.as_view()),
    path('tasks/', TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('', home, name='index'),
    path('tasks-page/', task_list_view, name='task_list'),
    path('feedback/', feedback_form, name='feedback_form' ),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', task_dashboard, name='task_dashboard'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
