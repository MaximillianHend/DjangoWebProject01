"""
Definition of forms.
"""

from django import forms
from .models import teacher, subject, school


class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']


class schoolForm(forms.ModelForm):
    class Meta:
        model = school
        fields = ['Name']


class subjectForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ['Name', 'Faculty']












from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
