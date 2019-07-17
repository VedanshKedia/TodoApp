from datetime import datetime
from django.shortcuts import render, get_object_or_404,redirect
from .models import TodoListItem
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import AddNewTodo
# from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


@login_required()
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    todolist = TodoListItem.objects.filter(creator=request.user)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', {'todoList': todolist})


def addnewtodo(request):
    # todo = get_object_or_404(AddNewTodo)
    if request.method == 'POST':
        form = AddNewTodo(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            # datetime = form.cleaned_data['datetime']
            priority = form.cleaned_data['priority']
            status = form.cleaned_data['status']

            todo = TodoListItem.objects.create(
                creator=request.user,
                todoTitle=title,
                todoDescription=description,
                todoDateTime=datetime.now(),
                priority=priority,
                status=status,
            )
            todo.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddNewTodo()
        return render(request, 'add_new_todo.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#
# def change_status(request):
#     TodoListItem.objects.filter()


def delete(request, pk):
    todo_item = get_object_or_404(TodoListItem, pk=pk)
    todo_item.delete()
    return HttpResponseRedirect(reverse('index'))


def delete_all(request):
    todo_item = TodoListItem.objects.filter(creator=request.user)
    todo_item.delete()
    return HttpResponseRedirect(reverse('index'))


def update_status(request, pk):
    todo_item = get_object_or_404(TodoListItem, pk=pk)
    if todo_item.status == 'Complete':
        todo_item.status = 'Incomplete'
        todo_item.save()
    else:
        todo_item.status = 'Complete'
        todo_item.save()
    return HttpResponseRedirect(reverse('index'))

