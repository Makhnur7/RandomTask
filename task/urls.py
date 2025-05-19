from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryCreateAPIView.as_view()),
    path('categories/<int:pk>', views.CategoryRetrieveUpdateDeleteAPIView.as_view()),
    path('difficulties/', views.DifficultyCreateAPIView.as_view()),
    path('tasks/', views.TaskCreateAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyAPIView.as_view())
]