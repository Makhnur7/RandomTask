from rest_framework import serializers

from .models import Category, Difficulty, Task


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class DifficultySerializers(serializers.ModelSerializer):

    class Meta:
        model = Difficulty
        fields = "__all__"

class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields =  "__all__"

        