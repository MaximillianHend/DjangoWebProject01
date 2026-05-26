"""
Definition of forms.
"""

from django import forms
from .models import teacher, subject


class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ['Name', 'Faculty']


