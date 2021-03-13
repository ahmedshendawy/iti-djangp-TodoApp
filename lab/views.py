from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
tasks = []

def index(request, name):
    return render(request, "mypro/index.html",
    {
        "name":name
    })

def addNew(request):
    if request.method == "POST":
        task = request.POST['task']
        tasks.append(task)
        return redirect('addNew')
    return render(request, "mypro/addNew.html",{
        "tasks":tasks,
    })

def delete(request):
    if request.POST.get('deleteTask'):
        task = request.POST['deleteTask']
        tasks.remove(task)
        return redirect('addNew')
    return render(request, "mypro/addNew.html",{
        "tasks":tasks,
    })