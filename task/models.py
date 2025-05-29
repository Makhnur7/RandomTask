from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'Категории'


class Difficulty(models.Model):

    level = models.CharField(max_length=100)
    # description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.level}"


    class Meta:
        verbose_name_plural = 'Сложность'


class Task(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE, verbose_name='Уровень')
    description = models.TextField(blank=True, verbose_name='Описание')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return f"{self.description}"
    
    class Meta:
        verbose_name_plural = 'Задания'

    

class Feedback(models.Model):

    name = models.CharField(max_length=190)
    email = models.EmailField()
    message = models.TextField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        verbose_name_plural = 'Комментарии'
    
    


