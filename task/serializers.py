from rest_framework import serializers

from .models import Category, Difficulty, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ['id', 'level']

class TaskSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    difficulty = serializers.CharField(source='difficulty.level', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'category', 'difficulty', 'answer']
