from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    


@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ('level',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'difficulty', 'answer')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

