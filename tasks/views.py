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


