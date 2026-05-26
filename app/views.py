"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .models import teacher, school, subject
from app.forms import subjectForm, schoolForm, teacherForm


def index(request):
    teach = teacher.objects.all()
    return render(request,"app/index.html",{'content': teach})

def index(request):
    sch = school.objects.all()
    return render(request,"app/index.html",{'content': sch})

def index(request):
    sub = subject.objects.all()
    return render(request,"app/index.html",{'content': sub})



def input_view(request):
    if request.method == "POST":
        form = teacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = teacherForm()

    return render(request, "app/teacher.html", {"form": form})




def input_view(request):
    if request.method == "POST":
        form = schoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = schoolForm()
    return render(request, "app/school.html", {"form": form})




def input_view(request):
    if request.method == "POST":
        form = subjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = subjectForm()
    return render(request, "app/subject.html", {"form": form})

