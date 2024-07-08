from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    Task = task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect("/")   
        
    context = {"Task":Task , "form":form}
    return render(request , "tasks/list.html" , context)

def updatetask(request ,pk ):
    Task =task.objects.get(id = pk)
    if request.method == "POSt":
         form = TaskForm( request.POST, instance=Task)
         if form.is_valid():
             form.save()
             return redirect("/")
        
    form = TaskForm(instance=Task)
    context={"form":form} 
    return render(request ,"tasks/update_task.html" , context)


def deleteTask(request ,pk ):
    items = task.objects.get(id = pk)
    if request.method == "POST":
        items.delete()
        return redirect("/")
        
    context = {"items":items}
    return render (request , "tasks/delete.html" , context)


