from django.shortcuts import render, redirect
from todoTask.models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, "mypro/index.html",{
        "tasks": tasks

    })

def create(request):
    if request.method == "POST":
        title=request.POST.get("taskTitle")
        descr=request.POST.get("taskDescr")
        prioirty=request.POST.get("taskPrioirty")
        comp = 0
        task = Task.objects.create(
            title=title,
            descr=descr,
            prioirty=prioirty,
            comp = comp
        )

        return redirect("index")

def update(request, id):
    task = Task.objects.get(pk=id)
    if request.method == "POST":
        title=request.POST.get("title")
        descr=request.POST.get("descr")
        prioirty=request.POST.get("prioirty")
        task.title = title
        task.descr = descr
        task.prioirty = prioirty
        task.save()
        return redirect("index")

def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()

    return redirect("index")