"""
Definition of forms.
"""

from django import forms
from .models import teacher, Outcome, subject


class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name', 'area']



class RubricForm(forms.Form):

    subject = forms.ModelChoiceField(queryset=subject.objects.all(),empty_label='Select a subject')
    outcomes = forms.ModelMultipleChoiceField(queryset=Outcome.objects.all(),widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['outcomes'].queryset = Outcome.objects.all()
