"""
Definition of views.
"""
#start of forms ----------------------->

from email.policy import default
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .models import teacher, subject, assessment, question, submission, mark
#from app.forms import subjectForm, teacherForm


#def index(request):
#    teach = teacher.objects.all()
#    sub = subject.objects.all()

#    return render(request,"app/index.html",{'subjects': sub, 'teachers': teach})




#def input_teacher(request):
 #   if request.method == "POST":
  #      form = teacherForm(request.POST)
   #     if form.is_valid():
    #        form.save()
   #         return redirect("index")
  #  else:
  #      form = teacherForm()
#
 #   return render(request, "app/teacher.html", {"form": form})



#def input_subject(request):
#    if request.method == "POST":
#        form = subjectForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("index")
#    else:
#        form = subjectForm()
#    return render(request, "app/subject.html", {"form": form})

#end of forms -------------------->



#Teacher Markings and Student Report card |
#                                         |
#                                        \/


#Teacher work flow

def create_assessment(request):
    form = assessmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("assessment_list")

    return render(request, "create_assessment.html", {"form": form})


#Questions for Assesments

def add_question(request, assessment_id):
    assessment = assessment.objects.get(id=assessment_id)
    form = questionForm(request.POST or None)

    if form.is_valid():
        question = form.save(commit=False)
        question.assessment = assessment
        question.save()
        return redirect("assessment_detail", assessment_id)

    return render(request, "add_question.html", {"form": form})
#"assessment": assessment 





#Markings System for Teachers

def mark_submission(request, submission_id):
    submission = submission.objects.get(id=submission_id)
    questions = submission.assessment.question_set.all()

    if request.method == "POST":
        for q in questions:
            score = request.POST.get(f"score_{q.id}")

            mark.objects.update_or_create(
            submission=submission_obj,
            question=q,
            defaults={"score": score}
        )

    return redirect("results", submission_id=submission_obj.id)

    return render(request, "mark_submission.html", {
    "submission": submission_obj,
    "questions": questions
    })



#Results Page for Students

def results(request, submission_id):
    submission = submission.objects.get(id=submission_id)
    marks = mark.objects.filter(submission=submission)


    total = sum(m.score for m in marks)

    return render(request, "results.html", {
        "submission": submission, 
        "marks": marks, 
        "total": total
        })


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
