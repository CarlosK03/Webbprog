from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cool(request):
    return render(request,"index1.html", {"lista":['banan','apelsin','äpple','godis','läsk']})

def carlos(request):
    return HttpResponse("<h1> Hej Carlos </h1>")

def brian(request):
    return HttpResponse("<h1> Hello Brian </h1>")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def greet(request, name):
    return render(request, "index.html", {"lista":['banan','apelsin','äpple','godis','läsk']}, {"name":name})

def frst(request):
    return render(request, "frstsitedjang.html")