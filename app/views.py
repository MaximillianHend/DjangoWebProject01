"""
Definition of views.
"""


from email.policy import default
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .assessments.services.rubric_generator import generate_rubric
from .models import Outcome, RubricTemplate, Criterion, PerformanceBand, teacher, subject
from app.forms import teacherForm, RubricForm


def rubric_view(request):

    print("VIEW HIT")
    if request.method == "POST":

        form = RubricForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            selected_outcomes = list(
                form.cleaned_data["outcomes"].values_list("code", flat=True)
                                    )

            print(selected_outcomes)
            rubric = generate_rubric(selected_outcomes)

            return render(request, "app/rubric.html", {"rubric": rubric})

        else:
            print(form.errors)

    else:

        form = RubricForm()

    return render(request, "app/rubric_form.html", {"form": form})


#start of forms ----------------------->
def index(request):
    teach = teacher.objects.all()

    return render(request,"app/index.html",{'teachers': teach})

def input_teacher(request):
    if request.method == "POST":
        form = teacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = teacherForm()

    return render(request, "app/teacher.html", {"form": form})


#end of forms -------------------->


#Generating PDF

from pypdf import PdfWriter, PdfReader #Joining PDFs
from reportlab.pdfgen import canvas #Generating PDfs
from reportlab.platypus import Paragraph,Image,Table #Generating PDfs
from django.http import FileResponse #Downloading files
from django.contrib.staticfiles.storage import staticfiles_storage #Working with static files
from io import BytesIO #Using Byte streams

def generate_pdf_file():
       
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]

    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)
   
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer


def report(request):
    pdf_file =  staticfiles_storage.path("EON15P-1_1_.pdf")

    try:
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf_file())        
        input2 = PdfReader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)
      
        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    except FileNotFoundError:
        response = FileResponse(generate_pdf_file(), as_attachment=True, filename="no.pdf")

    return response
