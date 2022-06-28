from django.shortcuts import render

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
            deadline = "2022-06-30"
        new_task = ToDoList.objects.create(title=title, status=status, deadline=deadline)
        context = {"plan": new_task}
        return render(request, 'index.html', context)

def task_view(request):
    pk = request.GET.get('pk')
    task = ToDoList.objects.get(pk=pk)
    return render(request, 'task_view.html', {'task':task})