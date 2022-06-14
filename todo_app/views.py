from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoItemForm


def index(request):
    context = {
        "tasks": ToDoItem.objects.all(),
    }
    return render(request, 'todo_app/index.html', context)


def about(request):
    return render(request, 'todo_app/about.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Incorrect data!"

    form = ToDoItemForm
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'todo_app/create.html', context)
