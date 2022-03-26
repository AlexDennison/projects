from django.shortcuts import redirect, render
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy 

#Class Based views

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_details'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'updateCbv.html'
    context_object_name = 'task'
    fields = ('taskname','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs = {'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your views here. Function Based Views
def add(request):
    task_details = Task.objects.all()
    if request.method == 'POST':
        taskname = request.POST.get('taskname',)
        priority = request.POST.get('priority',)
        date = request.POST.get('date')
        task = Task(taskname = taskname, priority = priority, date= date)
        task.save()
    return render(request,'home.html',{'task_details' : task_details})

def delete(request,id):
    task = Task.objects.get(id = id)
    if request.method =='post':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id= id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    
    return render(request,'update.html',{'task':task, 'f':f})