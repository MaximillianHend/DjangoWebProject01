from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
import app.views
import app


urlpatterns = [

    path('admin/', admin.site.urls),
    re_path(r'^$', app.views.index, name='index'),
    re_path(r'^home$', app.views.index, name='home'),
#    re_path(r'teacherinput', app.views.input_teacher, name='teacherinput'),
#    re_path(r'subjectinput', app.views.input_subject, name='subjectinput'),
    path('report/', app.views.report, name='report'),
]