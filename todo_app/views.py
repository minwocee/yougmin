from django.shortcuts import render, redirect
from .models import Todo
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404    #쿼리셋을 날리고 DB에 없으면 오류를 날린다.


def DeleteTodo(request, pk):
    delete_todo = get_object_or_404(Todo, pk=pk)
    delete_todo.delete()
    return redirect('/todo/')

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['todo', 'description', 'important']
              
    template_name = 'todo_app/todo_update_form.html'



class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['todo', 'description', 'important']

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

