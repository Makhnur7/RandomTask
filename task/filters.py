import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    difficulty = django_filters.CharFilter(field_name='difficulty__level', lookup_expr='icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')  # Для поиска по заголовку

    class Meta:
        model = Task
        fields = ['category', 'difficulty', 'title']
