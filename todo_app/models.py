from django.db import models

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=20)
    description = models.TextField()
    
    # 클래스 안에 만들어 준다.
    def __str__(self):
        return f'[{self.pk}] {self.todo}'
