from re import A
import app.models
from django.contrib import admin
from app.models import teacher, subject




# Register your models here.

admin.site.register(teacher)
admin.site.register(subject)