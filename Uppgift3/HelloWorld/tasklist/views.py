from django.shortcuts import render
from django.http import HttpResponse
from django import forms

tasklist=[] 

class NewTaskForm(forms.Form):
    task=forms.CharField(label="Add task")

# Create your views here.
def tasklist1(request):
    return render(request, "index.html")

def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasklist.append(task)
            return render(request, "index.html", {
                "tasklist":tasklist,
                "form":form
            })
        else:
            return render(request, "index.html", {
                "form":form    
            })
    return render(request, "index.html", {
        "form":NewTaskForm(),
        "tasklist":tasklist
        
    })
    