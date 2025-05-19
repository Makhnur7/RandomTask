from django.contrib import admin
from .models import Task, Category, Difficulty


admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Task)

