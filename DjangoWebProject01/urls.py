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
    re_path(r'^home$', app.views.index, name='home'),




#rubric paths
    re_path('generate_rubric/', app.views.rubric_view, name='rubric'),
    re_path("generate_rubric/", app.views.rubric_view, name='generate_rubric'),
    path('report/', app.views.report, name='report'),
    path('rubric/pdf/', app.views.generate_rubric_pdf, name='rubric_pdf'),


#input paths
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


#list paths
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


#id paths
    #single record display
    path('show_school/<school_id>', app.views.show_school, name="show_school"),

    #edit single record
    path('update_school/<school_id>', app.views.update_school, name="update_school"),

    #delete single record
    path('delete_school/<school_id>', app.views.delete_school, name="delete_school"),

]
    


