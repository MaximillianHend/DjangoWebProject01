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
import email
from .models import Outcome, RubricTemplate, Criterion, PerformanceBand, teacher, tblTeacher, tblSubject, tblSchool, tblStudent, tblCourse, tblMarkbook, tblAssessmentItem, tblUnit, tblEnrolment, tblSubmission
from app.forms import teacherForm, RubricForm, subjectForm, schoolForm, teacherForm, studentForm, courseForm, unitForm, assessmentitemForm, enrolmentForm, markbookForm, submissionForm
#from django.http.response import HttpResponseRedirect



#rubric generator code ---------------------------------------------------------------------------------
def rubric_view(request):

    print('VIEW HIT')

    form = RubricForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            tblSubject = form.cleaned_data['tblSubject']
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
    appName="Max's Django App for School Management"
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
    
    return render(request,'app/index.html',{"appName": appName,"objSchools":objSchools,"objTeachers":objTeachers,"objStudents":objStudents,"objSubjects":objSubjects,
                                            "objCourses":objCourses,"objUnits":objUnits,"objAssessmentItems":objAssessmentItems,"objEnrolments":objEnrolments,
                                            "objMarkbooks":objMarkbooks,"objSubmissions":objSubmissions})



# Individual record display
def show_school(request, school_id):
    school = tblSchool.objects.get(pk=school_id)
    return render(request, "app/show_school.html", {"school": school})  


def show_teacher(request, teacher_id):
    teacher = tblTeacher.objects.get(pk=teacher_id)
    return render(request, "app/show_teacher.html", {"teacher": teacher}) 


def show_student(request, student_id):
    student = tblStudent.objects.get(pk=student_id)
    return render(request, "app/show_student.html", {"student": student}) 


def show_subject(request, subject_id):
    subject = tblSubject.objects.get(pk=subject_id)
    return render(request, "app/show_subject.html", {"subject": subject}) 


def show_course(request, course_id):
    course = tblCourse.objects.get(pk=course_id)
    return render(request, "app/show_course.html", {"course": course}) 


def show_unit(request, unit_id):
    unit = tblUnit.objects.get(pk=unit_id)
    return render(request, "app/show_unit.html", {"unit": unit}) 


def show_assessmentitem(request, assessmentitem_id):
    assessmentitem = tblAssessmentItem.objects.get(pk=assessmentitem_id)
    return render(request, "app/show_assessmentitem.html", {"assessmentitem": assessmentitem}) 


def show_enrolment(request, enrolment_id):
    enrolment = tblEnrolment.objects.get(pk=enrolment_id)
    return render(request, "app/show_enrolment.html", {"enrolment": enrolment}) 


def show_markbook(request, markbook_id):
    markbook = tblMarkbook.objects.get(pk=markbook_id)
    return render(request, "app/show_markbook.html", {"markbook": markbook})  


def show_submission(request, submission_id):
    submission = tblSubmission.objects.get(pk=submission_id)
    return render(request, "app/show_submission.html", {"submission": submission}) 










email
# Clone records
def clone_school(request, school_id):
    original_school = tblSchool.objects.get(pk=school_id)
    cloned_school = tblSchool(SchoolName=f"Clone of {original_school.SchoolName}",Address=original_school.Address,
        Suburb=original_school.Suburb,State=original_school.State,Postcode=original_school.Postcode,Phone=original_school.Phone,
        Email=original_school,Website=original_school.Website)
    cloned_school.save()
    return redirect('schoollist')


def clone_teacher(request, teacher_id):
    original_teacher = tblTeacher.objects.get(pk=teacher_id)
    cloned_teacher = tblTeacher(FirstName=f"Clone of {original_teacher.FirstName}",LastName=f"Clone of {original_teacher.LastName}",
        Faculty=original_teacher.Faculty,Title=original_teacher.Title,Phone=original_teacher.Phone,Email=original_teacher.Email)
    cloned_teacher.save()
    return redirect('teacherlist')


def clone_student(request, student_id):
    original_student = tblStudent.objects.get(pk=student_id)
    cloned_student = tblStudent(FirstName=f"Clone of {original_student.FirstName}",LastName=f"Clone of {original_student.LastName}",
        Year=original_student.Year,Age=original_student.Age,Gender=original_student.Gender,Title=original_student.Title,
        DateOfBirth=original_student.DateOfBirth,Phone=original_student.Phone,Email=original_student.Email)
    cloned_student.save()
    return redirect('studentlist')


def clone_subject(request, subject_id):
    original_subject = tblSubject.objects.get(pk=subject_id)
    cloned_subject = tblSubject(SubjectName=f"Clone of {original_subject.SubjectName}",Area=original_subject.Area,Grade=original_subject.Grade)
    cloned_subject.save()
    return redirect('subjectlist')


def clone_course(request, course_id):
    original_course = tblCourse.objects.get(pk=course_id)
    cloned_course = tblCourse(CourseName=f"Clone of {original_course.CourseName}",Teacher=original_course.Teacher,School=original_course.School,
        Subject=original_course.Subject,CourseDesc=original_course.CourseDesc)
    cloned_course.save()
    return redirect('courselist')


def clone_unit(request, unit_id):
    original_unit = tblUnit.objects.get(pk=unit_id)
    cloned_unit = tblUnit(UnitName=f"Clone of {original_unit.UnitName}",UnitDesc=original_unit.UnitDesc,Course=original_unit.Course)
    cloned_unit.save()
    return redirect('unitlist')


def clone_assessmentitem(request, assessmentitem_id):
    original_assessmentitem = tblAssessmentItem.objects.get(pk=assessmentitem_id)
    cloned_assessmentitem = tblAssessmentItem(AssessmentItemName=f"Clone of {original_assessmentitem.AssessmentItemName}",Course=original_assessmentitem.Course,
        Unit=original_assessmentitem.Unit,Weighting=original_assessmentitem.Weighting)
    cloned_assessmentitem.save()
    return redirect('assessmentitemlist')


def clone_enrolment(request, enrolment_id):
    original_enrolment = tblEnrolment.objects.get(pk=enrolment_id)
    cloned_enrolment = tblEnrolment(EnrolmentName=f"Clone of {original_enrolment.EnrolmentName}",EnrolmentDate=original_enrolment.EnrolmentDate,School=original_enrolment.School,
        Course=original_enrolment.Course,Unit=original_enrolment.Unit,Student=original_enrolment.Student,StartDate=original_enrolment.StartDate,
        EndDate=original_enrolment.EndDate)
    cloned_enrolment.save()
    return redirect('enrolmentlist')


def clone_markbook(request, markbook_id):
    original_markbook = tblMarkbook.objects.get(pk=markbook_id)
    cloned_markbook = tblMarkbook(MarkbookName=f"Clone of {original_markbook.MarkbookName}",Teacher=original_markbook.Teacher,Course=original_markbook.Course,
        Unit=original_markbook.Unit,AssessmentItem=original_markbook.AssessmentItem,MarkValue=original_markbook.MarkValue,
        MarkDate=original_markbook.MarkDate,VET=original_markbook.VET)
    cloned_markbook.save()
    return redirect('markbooklist')


def clone_submission(request, submission_id):
    original_submission = tblSubmission.objects.get(pk=submission_id)
    cloned_submission = tblSubmission(SubmissionName=f"Clone of {original_submission.SubmissionName}",Markbook=original_submission.Markbook,Course=original_submission.Course,
        Unit=original_submission.Unit,AssessmentItem=original_submission.AssessmentItem,Student=original_submission.Student,
        SubmissionMark=original_submission.SubmissionMark,SubmissionDate=original_submission.SubmissionDate)
    cloned_submission.save()
    return redirect('submissionlist')







# Individual record update

def update_school(request, school_id):
    school = tblSchool.objects.get(pk=school_id)
    #form = schoolForm(request.POST or None, instance=school)
    return render(request, "app/update_school.html", {"school": school})
    #return render(request, "app/update_school.html", {"school": school}, {"form": form})
      
    '''
    form = schoolForm(request.POST or None, instance=school)
    if form.is_valid():
        form.save()
    return redirect('index')    
    '''

def update_teacher(request, teacher_id):
    teacher = tblTeacher.objects.get(pk=teacher_id)
    form = teacherForm(request.POST or None, instance=teacher)
    return render(request, "app/update_teacher.html", {"teacher": teacher})
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''
    
def update_student(request, student_id):
    student = tblStudent.objects.get(pk=student_id)
    form = studentForm(request.POST or None, instance=student)
    return render(request, "app/update_student.html", {"student": student})
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''

def update_subject(request, subject_id):
    subject = tblSubject.objects.get(pk=subject_id)
    form = subjectForm(request.POST or None, instance=subject)
    return render(request, "app/update_subject.html", {"subject": subject})
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''

def update_course(request, course_id):
    course = tblCourse.objects.get(pk=course_id)
    form = courseForm(request.POST or None, instance=course)
    return render(request, "app/update_course.html", {"course": course})
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''

def update_unit(request, unit_id):
    unit = tblUnit.objects.get(pk=unit_id)
    form = unitForm(request.POST or None, instance=unit)
    return render(request, "app/update_unit.html", {"unit": unit})
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''

def update_assessmentitem(request, assessmentitem_id):
    assessmentitem = tblAssessmentItem.objects.get(pk=assessmentitem_id)
    form = assessmentitemForm(request.POST or None, instance=assessmentitem)
    return render(request, "app/update_assessmentitem.html", {"assessmentitem": assessmentitem})
    
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''

def update_enrolment(request, enrolment_id):
    enrolment = tblEnrolment.objects.get(pk=enrolment_id)
    form = enrolmentForm(request.POST or None, instance=enrolment)
    return render(request, "app/update_enrolment.html", {"enrolment": enrolment})
    
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''

def update_markbook(request, markbook_id):
    markbook = tblMarkbook.objects.get(pk=markbook_id)
    form = markbookForm(request.POST or None, instance=markbook)
    return render(request, "app/update_markbook.html", {"markbook": markbook})
    
    '''
    if form.is_valid():
        form.save()
        return redirect('index')
    '''

def update_submission(request, submission_id):
    submission = tblSubmission.objects.get(pk=submission_id)
    form = submissionForm(request.POST or None, instance=submission)
    return render(request, "app/update_submission.html", {"submission": submission})
    
    '''
    if form.is_valid():
        form.save()
        return redirect('index')    
    '''
    





# Individual record delete
def delete_school(request, school_id):
    event = tblSchool.objects.get(pk=school_id)
    event.delete()
    return redirect('schoollist')


def delete_teacher(request, teacher_id):
    event = tblTeacher.objects.get(pk=teacher_id)
    event.delete()
    return redirect('teacherlist')


def delete_student(request, student_id):
    event = tblStudent.objects.get(pk=student_id)
    event.delete()
    return redirect('studentlist')


def delete_subject(request, subject_id):
    event = tblSubject.objects.get(pk=subject_id)
    event.delete()
    return redirect('subjectlist')


def delete_course(request, course_id):
    event = tblCourse.objects.get(pk=course_id)
    event.delete()
    return redirect('courselist')


def delete_unit(request, unit_id):
    event = tblUnit.objects.get(pk=unit_id)
    event.delete()
    return redirect('unitlist')


def delete_assessmentitem(request, assessmentitem_id):
    event = tblAssessmentItem.objects.get(pk=assessmentitem_id)
    event.delete()
    return redirect('assessmentitemlist')


def delete_enrolment(request, enrolment_id):
    event = tblEnrolment.objects.get(pk=enrolment_id)
    event.delete()
    return redirect('enrolmentlist')


def delete_markbook(request, markbook_id):
    event = tblMarkbook.objects.get(pk=markbook_id)
    event.delete()
    return redirect('markbooklist')


def delete_submission(request, submission_id):
    event = tblSubmission.objects.get(pk=submission_id)
    event.delete()
    return redirect('submissionlist')





# List Views for each model
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






# Multi-table Queries using select_related
def get_courses_with_subject():
    courses = tblCourse.objects.select_related('subject').all()
    for course in courses:
        print(course.CourseName, course.subject.SubjectName) 







# Data Entry Views for each model
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















def create_markbooks(request):
    units = tblUnit.objects.all()
    assessmentitems = tblAssessmentItem.objects.all()
    
    for teacher in tblTeacher.objects.all():

        for assessmentitem in assessmentitems:
            new_markbook = tblMarkbook(
                MarkbookName=f"New MB from {assessmentitem.AssessmentItemName}",
                Teacher=teacher.id,
                Course=assessmentitem.Course,
                Unit=assessmentitem.Unit,
                AssessmentItem=assessmentitem.id,
                MarkValue=assessmentitem.Weighting,
        )
        new_markbook.save()
    
    return redirect('index')

   

def return_home(request):
    return redirect('index')

def exit_app(request):
    quit
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

def return_home(request):
    return redirect('index')

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def login(request):
    return render(request, "app/login.html")

def exit_app(request):
    exit_app()