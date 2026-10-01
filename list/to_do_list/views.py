from django.shortcuts import render, redirect
from . models import Things

def Add(request):
    if request.method == "POST":
        task = request.POST.get("title")
        if task:
            Things.objects.create(name_task = task)
    tasks = Things.objects.all()

    return render(request, "interface.html", {"tasks": tasks})

def remove(request, id_task):
    task = Things.objects.get(id=id_task)
    tasks =Things.objects.all()
    task.delete()

def end(request, id_task):
    task = Things.objects.get(id=id_task)
    task.finish = True
    task.save()

def action(request, id_task):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "delete":
            remove(request, id_task)

        elif action == "end":
            end(request, id_task)
    return redirect("view")

def interface(request):
    tasks = Things.objects.all()
    return render(request, "interface.html", {"tasks": tasks})

