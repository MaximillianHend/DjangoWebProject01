from django.contrib import admin
from django.urls import include, re_path
from django.urls import path
from app import views
import app


urlpatterns = [

    path('admin/', admin.site.urls),
    re_path(r'^$', app.views.index, name='index'),
    re_path(r'^home$', app.views.index, name='home'),
]