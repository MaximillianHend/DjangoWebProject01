from re import A
import app.models
from django.contrib import admin
from app.models import teacher, Outcome, RubricTemplate, Criterion, PerformanceBand, tblTeacher, tblSubject, tblSchool, tblStudent, tblCourse, tblMarkbook, tblAssessmentItem, tblUnit, tblEnrolment, tblSubmission


#rubic models
admin.site.register(Outcome)
admin.site.register(RubricTemplate)
admin.site.register(Criterion)
admin.site.register(PerformanceBand)



#table models1
admin.site.register(tblTeacher)
admin.site.register(tblSubject)
admin.site.register(tblSchool)
admin.site.register(tblStudent)
admin.site.register(tblCourse)
admin.site.register(tblAssessmentItem)
admin.site.register(tblUnit)
admin.site.register(tblEnrolment)   
admin.site.register(tblMarkbook)
admin.site.register(tblSubmission)