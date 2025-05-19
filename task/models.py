from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'Categories'


class Difficulty(models.Model):

    level = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.level}"

    class Meta:
        verbose_name_plural = 'Difficulties'
    
class Task(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.name}"
    
    

    