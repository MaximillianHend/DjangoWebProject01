"""
Definition of models.
"""

from django.db import models
from django.shortcuts import render

#Create your models here.
class teacher(models.Model):
   name = models.CharField(max_length=100)
   area = models.CharField(max_length=30)

class subject(models.Model):
    name = models.CharField(max_length=100)



#Models for Rubric generator

class Outcome(models.Model):
    code = models.CharField(max_length=20)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    year_level = models.IntegerField()

class RubricTemplate(models.Model):
    assessment_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

class Criterion(models.Model):
    rubric = models.ForeignKey(RubricTemplate)
    name = models.CharField(max_length=200)

class PerformanceBand(models.Model):
    criterion = models.ForeignKey(Criterion)
    level = models.CharField(max_length=2)  # A/B/C/D/E
    descriptor = models.TextField()