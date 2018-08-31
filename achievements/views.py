from django.shortcuts import render, redirect, get_object_or_404

from .models import Task, Achievement
from .forms import TaskForm, AchievementForm
from itertools import chain

# Create your views here.
def index(request):
    results = {}
    total = 0
    lastest_task_list = Task.objects.all()
    for task in lastest_task_list:
        total = 0
        ftotal = 0
        ttotal = 0
        count = 0
        fcount = 0
        tcount = 0
        pb = 0
        results.setdefault(task.pk, []).append(task)
        for achievement in Achievement.objects.filter(task=task.pk, status=False):
            fcount+=1
            ftotal = ftotal+achievement.point
        for achievement in Achievement.objects.filter(task=task.pk, status=True):
            tcount+=1
            ttotal = ttotal+achievement.point
        for achievement in Achievement.objects.filter(task=task.pk):
            results[task.pk].append(achievement)
        count = fcount + tcount
        total = ftotal + ttotal
        pb = tcount / count * 100.0
        results[task.pk].append({'count':count, 'total':total, 'tcount':tcount, 'ttotal':ttotal, 'pb':pb})
    context = {'lastest_task_list':lastest_task_list,'results':results}
    return render(request, 'achievements/index.html', context)

def createtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return redirect('achievements:createachievement', task_id = task.pk)
    else:
        form = TaskForm()
    return render(request, 'achievements/task.html', {'form':form})

def createachievement(request, task_id):
    achievement = get_object_or_404(Task, pk = task_id)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            achievement = form.save(commit=False)
            t = Task.objects.get(pk=task_id)
            t.achievement_set.create(achievement=request.POST.get("achievement"), point=request.POST.get("point"))
            if 'add' in request.POST:          
                return redirect('achievements:createachievement',task_id = task_id)
            if 'finish' in request.POST:
                return redirect('achievements:index')
    else:
        form = AchievementForm(instance=achievement)
    t = Task.objects.get(pk=task_id)
    latest_achievement_list = t.achievement_set.all()
    return render(request, 'achievements/achievement.html', {'form':form, 'latest_achievement_list': latest_achievement_list})

def statusachievement(request, achievement_id, status):
    achievement = Achievement.objects.get(pk=achievement_id)
    achievement.status = status
    achievement.save()
    return redirect('achievements:index')