"""
Definition of models.
"""

from django.db import models
from django.shortcuts import render

#Create your models here.
class teacher(models.Model):
   name = models.CharField(max_length=100)
   area = models.CharField(max_length=100)

class subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Outcome(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    year_level = models.IntegerField()

class RubricTemplate(models.Model):
    assessment_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

class Criterion(models.Model):
    rubric = models.ForeignKey(RubricTemplate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class PerformanceBand(models.Model):
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    level = models.CharField(max_length=2) 
    descriptor = models.TextField()