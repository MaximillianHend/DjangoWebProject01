from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
import app.views
import app


urlpatterns = [

    path('admin/', admin.site.urls),
    re_path(r'^$', app.views.index, name='index'),
    re_path(r'^home$', app.views.index, name='home'),
    re_path(r'teacherinput', app.views.teacher_input, name='teacherinput'),
    #re_path(r'homeinput', app.views.input_view, name='homeinput'),
    re_path(r'subjectinput', app.views.subject_input, name='subjectinput'),
    path('report/', app.views.report, name='report'),
]