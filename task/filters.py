import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    difficulty = django_filters.CharFilter(field_name='difficulty__level', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')  

    class Meta:
        model = Task
        fields = ['category', 'difficulty', 'description']


