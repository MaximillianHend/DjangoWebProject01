from re import A
import app.models
from django.contrib import admin
from app.models import subject, teacher, Outcome, RubricTemplate, Criterion, PerformanceBand




# Register your models here.

#admin.site.register(teacher)
#admin.site.register(subject)
admin.site.register(Outcome)
admin.site.register(RubricTemplate)
admin.site.register(Criterion)
admin.site.register(PerformanceBand)
