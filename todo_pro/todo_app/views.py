from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    items = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('todo')
    else:
        form = TodoForm()

    page = {
        'forms': form,
        'list': items,
        'title': "Todo List"
    }
    return render(request,'index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'Task Removed!')
    return redirect('todo')
