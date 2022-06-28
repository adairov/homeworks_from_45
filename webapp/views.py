from django.shortcuts import render

# Create your views here.
from webapp.models import ToDoList


def index_view(request):
    plans = ToDoList.objects.all()
    context = {"plans": plans}
    return render(request, 'index.html', context)

def create_task(request):
    return render(request, 'create_task.html')