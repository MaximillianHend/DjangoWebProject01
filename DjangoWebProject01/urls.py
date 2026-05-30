from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
import app.views
import app


#    <p><a href="{% url 'report'%}">PDF report</a></p>
#link for pdf reports


urlpatterns = [
#general paths
    path('admin/', admin.site.urls),
    re_path(r'^$', app.views.index, name='index'),
#Navbar paths
    re_path(r'^home$', app.views.index, name='home'),
    re_path(r'^about$', app.views.about, name='about'),
    re_path(r'^contact$', app.views.contact, name='contact'),
    re_path(r'^login$', app.views.login, name='login'),


#rubric paths
    re_path('generate_rubric/', app.views.rubric_view, name='rubric'),
    re_path("generate_rubric/", app.views.rubric_view, name='generate_rubric'),
    path('report/', app.views.report, name='report'),
    path('rubric/pdf/', app.views.generate_rubric_pdf, name='rubric_pdf'),



#single record data entry display
    re_path(r'^schoolinput', app.views.input_school, name='schoolinput'),
    re_path(r'^teacherinput', app.views.input_teacher, name='teacherinput'),
    re_path(r'^studentinput', app.views.input_student, name='studentinput'),
    re_path(r'^subjectinput', app.views.input_subject, name='subjectinput'), 
    re_path(r'^courseinput', app.views.input_course, name='courseinput'),
    re_path(r'^unitinput', app.views.input_unit, name='unitinput'),
    re_path(r'^assessmentiteminput', app.views.input_assessmentitem, name='assessmentiteminput'),
    re_path(r'^enrolmentinput', app.views.input_enrolment, name='enrolmentinput'),
    re_path(r'^markbookinput', app.views.input_markbook, name='markbookinput'),
    re_path(r'^submissioninput', app.views.input_submission, name='submissioninput'),

#multiple record list display
    re_path(r'^schoollist', app.views.list_schools, name='schoollist'),
    re_path(r'^teacherlist', app.views.list_teachers, name='teacherlist'),
    re_path(r'^studentlist', app.views.list_students, name='studentlist'),
    re_path(r'^subjectlist', app.views.list_subjects, name='subjectlist'),
    re_path(r'^courselist', app.views.list_courses, name='courselist'),
    re_path(r'^unitlist', app.views.list_units, name='unitlist'),
    re_path(r'^assessmentitemlist', app.views.list_assessmentitems, name='assessmentitemlist'),
    re_path(r'^enrolmentlist', app.views.list_enrolments, name='enrolmentlist'),
    re_path(r'^markbooklist', app.views.list_markbooks, name='markbooklist'),
    re_path(r'^submissionlist', app.views.list_submissions, name='submissionlist'),

    #single record display
    path('show_school/<school_id>', app.views.show_school, name="show_school"),
    path('show_teacher/<teacher_id>', app.views.show_teacher, name="show_teacher"),
    path('show_student/<student_id>', app.views.show_student, name="show_student"),
    path('show_subject/<subject_id>', app.views.show_subject, name="show_subject"),
    path('show_course/<course_id>', app.views.show_course, name="show_course"),
    path('show_unit/<unit_id>', app.views.show_unit, name="show_unit"),
    path('show_assessmentitem/<assessmentitem_id>', app.views.show_assessmentitem, name="show_assessmentitem"),
    path('show_enrolment/<enrolment_id>', app.views.show_enrolment, name="show_enrolment"),
    path('show_markbook/<markbook_id>', app.views.show_markbook, name="show_markbook"),
    path('show_submission/<submission_id>', app.views.show_submission, name="show_submission"),

    #edit single record
    path('update_school/<school_id>', app.views.update_school, name="update_school"),
    path('update_teacher/<teacher_id>', app.views.update_teacher, name="update_teacher"),
    path('update_student/<student_id>', app.views.update_student, name="update_student"),
    path('update_subject/<subject_id>', app.views.update_subject, name="update_subject"),
    path('update_course/<course_id>', app.views.update_course, name="update_course"),
    path('update_unit/<unit_id>', app.views.update_unit, name="update_unit"),
    path('update_assessmentitem/<assessmentitem_id>', app.views.update_assessmentitem, name="update_assessmentitem"),
    path('update_enrolment/<enrolment_id>', app.views.update_enrolment, name="update_enrolment"),
    path('update_markbook/<markbook_id>', app.views.update_markbook, name="update_markbook"),
    path('update_submission/<submission_id>', app.views.update_submission, name="update_submission"),

    #delete single record
    path('delete_school/<school_id>', app.views.delete_school, name="delete_school"),
    path('delete_teacher/<teacher_id>', app.views.delete_teacher, name="delete_teacher"),
    path('delete_student/<student_id>', app.views.delete_student, name="delete_student"),
    path('delete_subject/<subject_id>', app.views.delete_subject, name="delete_subject"),
    path('delete_course/<course_id>', app.views.delete_course, name="delete_course"),
    path('delete_unit/<unit_id>', app.views.delete_unit, name="delete_unit"),
    path('delete_assessmentitem/<assessmentitem_id>', app.views.delete_assessmentitem, name="delete_assessmentitem"),
    path('delete_enrolment/<enrolment_id>', app.views.delete_enrolment, name="delete_enrolment"),
    path('delete_markbook/<markbook_id>', app.views.delete_markbook, name="delete_markbook"),
    path('delete_submission/<submission_id>', app.views.delete_submission, name="delete_submission"),

    #clone single record
    path('clone_school/<school_id>', app.views.clone_school, name="clone_school"),
    path('clone_teacher/<teacher_id>', app.views.clone_teacher, name="clone_teacher"),
    path('clone_student/<student_id>', app.views.clone_student, name="clone_student"),
    path('clone_subject/<subject_id>', app.views.clone_subject, name="clone_subject"),
    path('clone_course/<course_id>', app.views.clone_course, name="clone_course"),
    path('clone_unit/<unit_id>', app.views.clone_unit, name="clone_unit"),
    path('clone_assessmentitem/<assessmentitem_id>', app.views.clone_assessmentitem, name="clone_assessmentitem"),
    path('clone_enrolment/<enrolment_id>', app.views.clone_enrolment, name="clone_enrolment"),
    path('clone_markbook/<markbook_id>', app.views.clone_markbook, name="clone_markbook"),
    path('clone_submission/<submission_id>', app.views.clone_submission, name="clone_submission"),

    #create markbooks from existing data
    path('create_markbooks', app.views.create_markbooks, name="create_markbooks"),

    #Nav Bar buttons
    path('return_home', app.views.return_home, name="return_home"),
    path('exit_app', app.views.return_home, name="exit_app"),
    
]
    


