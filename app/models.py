"""
Definition of models.
"""

from django.db import models
from django.shortcuts import render
from email.headerregistry import Address, Group
from email.policy import default
from tarfile import NUL
from tkinter import FIRST, PhotoImage
from turtle import isvisible
from datetime import date

#rubric models---------------------------------------------------------------
class teacher(models.Model):
   name = models.CharField(max_length=100)
   area = models.CharField(max_length=100)





class Outcome(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField()
    tblSubject = models.CharField(max_length=100)
    year_level = models.IntegerField()
    def __str__(self):
        return self.code


class RubricTemplate(models.Model):
    assessment_type = models.CharField(max_length=100)
    tblSubject = models.CharField(max_length=100)


class Criterion(models.Model):
    rubric = models.ForeignKey(RubricTemplate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class PerformanceBand(models.Model):
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    level = models.CharField(max_length=2) 
    descriptor = models.TextField()
#--------------------------------------------------------------------------------------------


#table models--------------------------------------------------------------------------------

class tblSchool(models.Model):
    SchoolNbr = models.CharField(max_length=10, default='S0000')
    SchoolName = models.CharField(max_length=25)
    Address = models.CharField(max_length=50, null=True)
    Suburb = models.CharField(max_length=30)
    State = models.CharField(max_length=3, null=True) 
    Postcode = models.CharField(max_length=10, null=True)  
    Phone = models.CharField(max_length=20, null=True)
    Email = models.CharField(max_length=50, null=True)
    Website = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.SchoolNbr + ": " + self.SchoolName
       
    
class tblTeacher(models.Model):
    TeacherNbr = models.CharField(max_length=10, default='T0000')
    FirstName = models.CharField(max_length=25)     
    LastName = models.CharField(max_length=25) 
    Faculty = models.CharField(max_length=30, null=True)
    Title = models.CharField(max_length=30, null=True) 
    Phone = models.CharField(max_length=20, null=True)
    Email = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.TeacherNbr + ": " + self.LastName + ", " + self.FirstName
    

class tblStudent(models.Model):
    StudentNbr = models.CharField(max_length=10,default='ST0000')
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Year = models.CharField(max_length=30)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10, null=True) 
    Title = models.CharField(max_length=30)
    DateOfBirth = models.DateField(null=True)
    Phone = models.CharField(max_length=20, null=True)
    Email = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.StudentNbr + ": " + self.LastName + ", " + self.FirstName

  
   
class tblSubject(models.Model):
    SubjectNbr = models.CharField(max_length=10, default='SB0000')
    SubjectName = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
    Grade = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.SubjectNbr + ": " + self.SubjectName
    

class tblCourse(models.Model):
    CourseNbr = models.CharField(max_length=10, default='C0000')
    CourseName = models.CharField(max_length=25)
    Teacher = models.ForeignKey(tblTeacher, on_delete=models.CASCADE, related_name='Teacher')
    School = models.ForeignKey(tblSchool, on_delete=models.CASCADE, related_name='School')
    Subject = models.ForeignKey(tblSubject, on_delete=models.CASCADE, related_name='Subject')
    CourseDesc = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.CourseNbr + ": " + self.CourseName


class tblUnit(models.Model):
    UnitNbr = models.CharField(max_length=10, default='U0000')
    UnitName = models.CharField(max_length=25)
    Course = models.ForeignKey(tblCourse, on_delete=models.CASCADE, related_name='Course')
    UnitDesc = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.UnitNbr + ": " + self.UnitName


class tblAssessmentItem(models.Model):
    AssessmentItemNbr = models.CharField(max_length=10, default='AI0000')
    AssessmentItemName = models.CharField(max_length=25)
    Course = models.ForeignKey(tblCourse, on_delete=models.CASCADE, related_name='UnitCourse')
    Unit = models.ForeignKey(tblUnit, null=True, on_delete=models.CASCADE, related_name='Unit')
    Weighting = models.IntegerField()
    def __str__(self):
        return self.AssessmentItemNbr + ": " + self.AssessmentItemName


class tblEnrolment(models.Model):
    EnrolmentNbr = models.CharField(max_length=10, default='E0000')
    EnrolmentName = models.CharField(max_length=25)
    EnrolmentDate = models.DateField(default=date.today)
    School = models.ForeignKey(tblSchool, null=True, on_delete=models.CASCADE, related_name='EnrolSchool')
    Subject = models.ForeignKey(tblSubject, null=True, on_delete=models.CASCADE, related_name='EnrolSubject')
    Course = models.ForeignKey(tblCourse, null=True, on_delete=models.CASCADE, related_name='EnrolCourse')
    Unit = models.ForeignKey(tblUnit, null=True, on_delete=models.CASCADE, related_name='EnrolUnit')
    Student = models.ForeignKey(tblStudent, on_delete=models.CASCADE, related_name='EnrolStudent')
    StartDate = models.DateField(null=True)
    EndDate = models.DateField(null=True)
    def __str__(self):
        return self.EnrolmentNbr + ": " + self.EnrolmentDate.strftime("%d-%m-%Y")


class tblMarkbook(models.Model):
    MarkbookNbr = models.CharField(max_length=10, default='MB0000')
    MarkbookName = models.CharField(max_length=25)
    Teacher = models.ForeignKey(tblTeacher, null=True, on_delete=models.CASCADE, related_name='MarkbookTeacher')
    Course = models.ForeignKey(tblCourse, on_delete=models.CASCADE, related_name='MarkbookCourse')
    Unit = models.ForeignKey(tblUnit, null=True, on_delete=models.CASCADE, related_name='MarkbookUnit') 
    AssessmentItem = models.ForeignKey(tblAssessmentItem, null=True, on_delete=models.CASCADE, related_name='MarkbookAI')
    MarkValue = models.IntegerField()
    MarkDate = models.DateField(default=date.today)
    VET = models.BooleanField(default=False)    
    def __str__(self):
        return self.MarkbookNbr + ": " + self.MarkbookName
       

class tblSubmission(models.Model):
    SubmissionNbr = models.CharField(max_length=10, default='S0000')
    SubmissionName = models.CharField(max_length=25)
    Markbook = models.ForeignKey(tblMarkbook, on_delete=models.CASCADE, related_name='SubmissionMarkbook')
    Course = models.ForeignKey(tblCourse, on_delete=models.CASCADE, related_name='SubmissionCourse')
    Unit = models.ForeignKey(tblUnit, null=True, on_delete=models.CASCADE, related_name='SubmissionUnit')
    Student = models.ForeignKey(tblStudent, on_delete=models.CASCADE, related_name='SubmissionStudent')
    AssessmentItem = models.ForeignKey(tblAssessmentItem, on_delete=models.CASCADE, related_name='SubmissionAI')
    SubmissionMark = models.IntegerField()
    SubmissionDate = models.DateField(default=date.today)
    def __str__(self):
        return self.SubmissionNbr + ": " + self.SubmissionDate.strftime("%d-%m-%Y")

