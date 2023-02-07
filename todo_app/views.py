from django.shortcuts import render
from .models import Todo
# Create your views here.

def Todos(request):
    #필터를 추가한다.(내림차순으로 정렬한다.)
    todos = Todo.objects.all().order_by('-pk')

    return render(
        request, 
        'todo_app/todos.html',
        {   
            #todos 를 html 변수에 넣어주는 과정
            'todos' : todos,
        }
        
        )

