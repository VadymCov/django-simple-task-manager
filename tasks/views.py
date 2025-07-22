from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tasks

# Home page: display all tasks
def index(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks, 'title':'home page'}
    return render(request, 'tasks/index.html', context)

# Processing adding a new task via POST request
@require_POST
def add(request):
    if title := request.POST.get('title'):
       Tasks.objects.create(title=title)
    return redirect('index')

# Update status task completed/ no completed
def update(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('index')
# Delete task by ID
def delete(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('index')