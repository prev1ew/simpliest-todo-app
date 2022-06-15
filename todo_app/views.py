from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoItemForm


def index(request):
    filter_value = 0
    if request.method == 'GET':
        filter_value = int(request.GET.get('filter', 0))

    context = {
        "tasks": ToDoItem.objects.all() if not filter_value else
        ToDoItem.objects.filter(is_completed=(True if filter_value == 1 else False)),
        'filter': filter_value
    }
    return render(request, 'todo_app/index.html', context)


def about(request):
    has_data = bool(len(ToDoItem.objects.all()))
    context = {'has_data': has_data}
    return render(request, 'todo_app/about.html', context)


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
        'error': error,
        'method': 'create'
    }

    return render(request, 'todo_app/todo_item_form.html', context)


def change_todo_item(request, pk):
    curr_item = ToDoItem.objects.get(id=pk)
    form = ToDoItemForm(instance=curr_item)
    if request.method == 'POST':
        form = ToDoItemForm(request.POST, request.FILES, instance=curr_item)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'method': 'change'
    }
    return render(request, 'todo_app/todo_item_form.html', context)


def delete_todo_item(request, pk):
    curr_item = ToDoItem.objects.get(id=pk)
    if request.method == 'POST':
        print(curr_item)
        curr_item.delete()
        return redirect('index')

    context = {'item': curr_item}
    return render(request, 'todo_app/delete_item.html')
