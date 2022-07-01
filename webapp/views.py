from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from webapp.models import ToDoList, STATUS_CHOICES


def index_view(request):
    plans = ToDoList.objects.all()
    context = {"plans": plans}
    return render(request, 'index.html', context)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {"statuses": STATUS_CHOICES})
    else:
        title = request.POST.get("title"),
        status = request.POST.get("status")
        if request.POST.get("deadline"):
            deadline = request.POST.get("deadline")
        else:
            deadline = None
        description = request.POST.get("description")
        new_task = ToDoList.objects.create(title=title, status=status, deadline=deadline, description=description)
        return redirect("view", pk=new_task.pk)

def task_view(request, pk):
    # pk = request.GET.get('pk')
    task = ToDoList.objects.get(pk=pk)
    return render(request, 'task_view.html', {'task':task})

def update_task(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        return render(request, 'update_task.html', {"task": task})
    else:
        task.title = request.POST.get("title"),
        task.status = request.POST.get("status")
        task.deadline = request.POST.get("deadline")
        task.description = request.POST.get("description")
        task.save()
        return redirect("view", pk=task.pk)

def delete_task(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', {"task": task})
    else:
        task.delete()
        return redirect("index")