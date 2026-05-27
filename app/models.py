"""
Definition of models.
"""

from django.db import models
from django.shortcuts import render

#Create your models here.
class teacher(models.Model):
   name = models.CharField(max_length=100)
   area = models.CharField(max_length=30)


class student(models.Model):
    name = models.CharField(max_length=100)
    

class subject(models.Model):
    name = models.CharField(max_length=100)


class assessment(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    

class question(models.Model):
    assessment = models.ForeignKey(assessment, on_delete=models.CASCADE)
    text = models.TextField()
    max_marks = models.IntegerField()


class submission(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    assessment = models.ForeignKey(assessment, on_delete=models.CASCADE)


class mark(models.Model):
    submission = models.ForeignKey(submission, on_delete=models.CASCADE)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    score = models.IntegerField()