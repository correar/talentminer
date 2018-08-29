from django.shortcuts import render, redirect

from .models import Task, Achievement
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            lastest_task_list = Task.objects.all()
            return render(request, 'achievements/index.html', {'form':form, 'lastest_task_list':lastest_task_list})
    else:
        form = TaskForm()
    lastest_task_list = Task.objects.all()
    return render(request, 'achievements/index.html', {'form':form, 'lastest_task_list':lastest_task_list})