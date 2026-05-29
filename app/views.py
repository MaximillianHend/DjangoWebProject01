"""
Definition of views.
"""


from email.policy import default
import html
import http
import re
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .assessments.services.rubric_generator import generate_rubric
from .models import Outcome, RubricTemplate, Criterion, PerformanceBand, teacher, subject, tblTeacher, tblSubject, tblSchool, tblStudent, tblCourse, tblMarkbook, tblAssessmentItem, tblUnit, tblEnrolment, tblSubmission
from app.forms import teacherForm, RubricForm, subjectForm, schoolForm, teacherForm, studentForm, courseForm, unitForm, assessmentitemForm, enrolmentForm, markbookForm, submissionForm
#from django.http.response import HttpResponseRedirect



#rubric generator code ---------------------------------------------------------------------------------
def rubric_view(request):

    print('VIEW HIT')

    form = RubricForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            subject = form.cleaned_data['subject']
            selected_outcomes = list(form.cleaned_data['outcomes'].values_list('code', flat=True))
            rubric = generate_rubric(selected_outcomes)
            request.session['rubric'] = rubric

            return render(request,'app/rubric.html',{'rubric': rubric})

        else:
            print(form.errors)

    return render(request,'app/rubric_form.html',{'form': form})

#-----------------------------------------------------------------------------------------------------






#generals defs-----------------------------------------------------------------------------------------
def index(request):
    appName="Task 3 Final Build" 
    objSchools = tblSchool.objects.all()
    objTeachers = tblTeacher.objects.all()
    objStudents = tblStudent.objects.all()
    objSubjects = tblSubject.objects.all()
    objCourses = tblCourse.objects.all()
    objUnits = tblUnit.objects.all()
    objAssessmentItems = tblAssessmentItem.objects.all()
    objEnrolments = tblEnrolment.objects.all()
    objMarkbooks = tblMarkbook.objects.all()
    objSubmissions = tblSubmission.objects.all()
    
    return render(request,'app/index.html',{"appName": appName,"objSchools":objSchools,"objTeachers":objTeachers,"objStudents":objStudents,
                                            "objSubjects":objSubjects,"objCourses":objCourses,"objUnits":objUnits,"objAssessmentItems":objAssessmentItems,
                                            "objEnrolments":objEnrolments,"objMarkbooks":objMarkbooks,"objSubmissions":objSubmissions,})



def show_school(request, school_id):
    school = tblSchool.objects.get(id=school_id)
    return render(request, "app/show_school.html", {"school": school})  


def update_school(request, school_id):
    school = tblSchool.objects.get(pk=school_id)
    form = schoolForm(request.POST or None, instance=school)
    if form.is_valid():
        form.save()
        return render(request,"app/listSchools.html",{"school": school})



def delete_school(request, school_id):
    event = tblSchool.objects.get(id=school_id)
    event.delete()
    return redirect('schoollist')


def get_courses_with_subject():
    courses = tblCourse.objects.select_related('subject').all()
    for course in courses:
        print(course.CourseName, course.subject.SubjectName)
#---------------------------------------------------------------------------------------------------------






# list views for each model -------------------------------------------------------------------------------
def list_schools(request):
    lstSchools = tblSchool.objects.all()
    return render(request, "app/listSchools.html", {"lstSchools": lstSchools})
    
def list_teachers(request):
    lstTeachers = tblTeacher.objects.all()
    return render(request, "app/listTeachers.html", {"lstTeachers": lstTeachers})

def list_students(request):
    lstStudents = tblStudent.objects.all()
    return render(request, "app/listStudents.html", {"lstStudents": lstStudents})

def list_subjects(request):
    lstSubjects = tblSubject.objects.all()
    return render(request, "app/listSubjects.html", {"lstSubjects": lstSubjects})

def list_courses(request):
    lstCourses = tblCourse.objects.all()
    return render(request, "app/listCourses.html", {"lstCourses": lstCourses})

def list_units(request):
    lstUnits = tblUnit.objects.all()
    return render(request, "app/listUnits.html", {"lstUnits": lstUnits})

def list_assessmentitems(request):
    lstAssessmentItems = tblAssessmentItem.objects.all()
    return render(request, "app/listAssessmentItems.html", {"lstAssessmentItems": lstAssessmentItems})

def list_enrolments(request):
    lstEnrolments = tblEnrolment.objects.all()
    return render(request, "app/listEnrolments.html", {"lstEnrolments": lstEnrolments})

def list_markbooks(request):
    lstMarkbooks = tblMarkbook.objects.all()
    return render(request, "app/listMarkbooks.html", {"lstMarkbooks": lstMarkbooks})

def list_submissions(request):
    lstSubmissions = tblSubmission.objects.all()
    return render(request, "app/listSubmissions.html", {"lstSubmissions": lstSubmissions})
#---------------------------------------------------------------------------------------------------------------





# inputs for school, teacher, student, subject, course, unit, assessment item, enrolment, markbook, submission

def input_school(request):
    submitted = False
    
    if request.method == "POST":
        form = schoolForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = schoolForm()
        if submitted in request.GET:
            submitted = True
    return render(request, "app/school.html", {"form": form})



def input_teacher(request):
    if request.method == "POST":
        form = teacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = teacherForm()

    return render(request, "app/teacher.html", {"form": form})



def input_student(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = studentForm()
    return render(request, "app/student.html", {"form": form})



def input_subject(request):

    if request.method == "POST":
        form = subjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = subjectForm()
    return render(request, "app/subject.html", {"form": form})



def input_course(request):
    if request.method == "POST":
        form = courseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = courseForm()
    return render(request, "app/course.html", {"form": form})



def input_unit(request):
    if request.method == "POST":
        form = unitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = unitForm()
    return render(request, "app/unit.html", {"form": form})



def input_assessmentitem(request):
    if request.method == "POST":
        form = assessmentitemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = assessmentitemForm()
    return render(request, "app/assessmentitem.html", {"form": form})



def input_enrolment(request):
    if request.method == "POST":
        form = enrolmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = enrolmentForm()
    return render(request, "app/enrolment.html", {"form": form})



def input_markbook(request):
    if request.method == "POST":
        form = markbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = markbookForm()
    return render(request, "app/markbook.html", {"form": form})



def input_submission(request):
    if request.method == "POST":
        form = submissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = submissionForm()
    return render(request, "app/submission.html", {"form": form})

#-----------------------------------------------------------------------------------------------------




#Generating PDFs -------------------------------------------------------------------------------------

from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas 
from reportlab.platypus import Paragraph,Image,Table 
from django.http import FileResponse 
from django.contrib.staticfiles.storage import staticfiles_storage 
from io import BytesIO 
from django.template.loader import render_to_string 
from weasyprint import HTML



def generate_rubric_pdf(request):

    rubric = request.session.get('rubric')
    html_string = render_to_string('app/rubric_pdf.html',{'rubric': rubric})
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file,content_type='application/pdf')
    response['Content-Disposition'] = ('attachment; filename="rubric.pdf"')

    return response




def generate_pdf_file():
       
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]

    teachers = teacher.objects.all()

    for teach in teachers:
        lines.append((teach.name, teach.area))

    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)
   
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer


def report(request):
    pdf_file =  staticfiles_storage.path('EON15P-1_1_.pdf')

    try:
        merger = PdfWriter()

        input1 = PdfReader(generate_pdf_file())        
        input2 = PdfReader(pdf_file, 'rb')

        merger.append(input1)
        merger.append(input2)
      
        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment=True, filename='hello.pdf')
    except FileNotFoundError:
        response = FileResponse(generate_pdf_file(), as_attachment=True, filename='no.pdf')

    return response

#----------------------------------------------------------------------------------------------------