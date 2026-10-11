from django.shortcuts import render
from .models import Task  # call task to interface
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required

#force login page to show befor home page
@login_required
def home(request):
# Handle only the current user's tasks............................................................
    tasks = Task.objects.filter(user=request.user) 
    return render(request, 'home.html', {'tasks':tasks})

#...........................add task def.....................................
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) 
            task.user = request.user       
            task.save()                   
            return redirect('home')
    else:
        form = TaskForm()
    return render (request, 'add_task.html', {'form':form})

#...........................edit task def....................................
def edit_task(request, task_id):
    task =get_object_or_404(Task, id= task_id)

    if task.user != request.user: # ← إذا لم تكن للمستخدم الحالي
        return HttpResponseForbidden('Not Your Task!!')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = TaskForm (instance=task)
    
    return render(request, 'edit_task.html',{'form':form, 'task':task})

#...........................delete task def..................................
@permission_required('pages.can_delete_task', raise_exception=True)
def delete_task(request,task_id):
    task =get_object_or_404(Task, id= task_id)

    if task.user != request.user:  # ← إذا لم تكن للمستخدم الحالي
        return HttpResponseForbidden('Not Your Task!!')
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
    return render(request, 'delete_task.html',{'task': task})

