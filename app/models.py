"""
Definition of models.
"""

from django.db import models
from django.shortcuts import render

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)


class subject(models.Model):
    Name = models.CharField(max_length=25)
    Faculty = models.CharField(max_length=30)
    