from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def daily_tasks_home(request):
    # Notice the '.filter(is_completed=False)' - this ensures finished tasks disappear from the list!
    daily_tasks = Task.objects.filter(task_type='DAILY', is_completed=False)
    
    context = {
        'tasks': daily_tasks
    }
    return render(request, 'tasks/home.html', context)

def complete_task(request, task_id):
    # 1. Grab the specific task by its ID
    task = get_object_or_404(Task, id=task_id)
    
    # 2. If someone clicks the button (which sends a POST request), mark it done
    if request.method == 'POST':
        task.is_completed = True
        task.save()
        
    # 3. Refresh the home page instantly so the task disappears
    return redirect('home')