"""
Definition of forms.
"""

from django import forms
from .models import teacher, Outcome, tblSchool, tblTeacher, tblStudent, tblSubject, tblCourse, tblUnit, tblAssessmentItem, tblEnrolment, tblMarkbook, tblSubmission
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.forms import widgets, ModelForm



#unused forms ---------------------------------------------------------------------------------------
class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name', 'area']



#rubric forms ---------------------------------------------------------------------------------------
class RubricForm(forms.Form):

    tblSubject = forms.ModelChoiceField(queryset=tblSubject.objects.all(),empty_label='Select a subject')
    outcomes = forms.ModelMultipleChoiceField(queryset=Outcome.objects.all(),widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['outcomes'].queryset = Outcome.objects.all()
#-----------------------------------------------------------------------------------------------------




#webpage forms -------------------------------------------------------------------------------------------------------------------
class schoolForm(forms.ModelForm):
    class Meta:
        model = tblSchool
        fields = ('SchoolNbr','SchoolName','Address','Suburb','State','Postcode','Phone','Email','Website')
        labels = {'SchoolNbr': "",'SchoolName': "",'Address': "",'Suburb': "",'State': "",'Postcode': "",'Phone': "",'Email': "",'Website': "",}
        widgets = {
            'SchoolNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Number'}),
            'SchoolName': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Name'}),
            'Address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Address'}),
            'Suburb': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Suburb'}),
            'State': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School State'}),
            'Postcode': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Postcode'}),    
            'Phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Phone'}),
            'Email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Email'}),
            'Website': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Website'}),
            }
        
        
class teacherForm(forms.ModelForm):
    class Meta:
        model = tblTeacher
        fields = ['TeacherNbr','Title','FirstName','LastName','Faculty','Phone','Email']
        labels = {'TeacherNbr': "Tch Nbr",'Title': "Title",'FirstName': "FirstName",'LastName': "LastName",'Faculty': "Faculty",'Phone': "Phone",'Email': "Email",}
        widgets = {
            'TeacherNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter School Number'}),
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Faculty': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            }

class studentForm(forms.ModelForm):
    class Meta:
        model = tblStudent
        fields = ['StudentNbr','FirstName','LastName','Year','Age','Gender','Title','DateOfBirth','Phone','Email'] 
        labels = {'StudentNbr': "St Nbr",'FirstName': "FirstName",'LastName': "LastName",'Year': "Year",'Age': "Age",'Gender':"",'Title': "Title",'DateOfBirth': "DOB",'Phone': "Phone",'Email': "Email",}
        widgets = {
            'StudentNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Student Number'}),
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Year': forms.TextInput(attrs={'class': 'form-control'}),
            'Age': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control'}),
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'DateOfBirth': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            }

class subjectForm(forms.ModelForm):
    class Meta:
        model = tblSubject
        fields = ['SubjectNbr','SubjectName','Area','Grade'] 
        labels = {'SubjectNbr': "Sub Nbr",'SubjectName': "Subject Name",'Area': "Area",'Grade': "Grade",}
        widgets = {
            'SubjectNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Subject Number'}),
            'SubjectName': forms.TextInput(attrs={'class': 'form-control'}),
            'Area': forms.TextInput(attrs={'class': 'form-control'}),
            'Grade': forms.TextInput(attrs={'class': 'form-control'}),
            }

class courseForm(forms.ModelForm):
    class Meta:
        model = tblCourse
        fields = ['CourseNbr','CourseName','CourseDesc','Subject', 'School','Teacher']
        labels = {'CourseNbr': "Crs Nbr",'CourseName': "Course Name",'CourseDesc': "Course Description",'Subject': "Subject",'School': "School",'Teacher': "Teacher",}
        widgets = {
            'CourseNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Course Number'}),
            'CourseName': forms.TextInput(attrs={'class': 'form-control'}),
            'CourseDesc': forms.TextInput(attrs={'class': 'form-control'}),
            'Subject': forms.Select(attrs={'class': 'form-control'}),
            'School': forms.Select(attrs={'class': 'form-control'}),
            'Teacher': forms.Select(attrs={'class': 'form-control'}),
            }

class unitForm(forms.ModelForm):
    class Meta:
        model = tblUnit
        fields = ['UnitNbr','UnitName','Course','UnitDesc'] 
        labels = {'UnitNbr': "Unit Nbr",'UnitName': "Unit Name",'Course': "Course",'UnitDesc': "Unit Description",}
        widgets = {
            'UnitNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Unit Number'}),
            'UnitName': forms.TextInput(attrs={'class': 'form-control'}),
            'Course': forms.Select(attrs={'class': 'form-control'}),
            'UnitDesc': forms.TextInput(attrs={'class': 'form-control'}),
            }

class assessmentitemForm(forms.ModelForm):
    class Meta:
        model = tblAssessmentItem
        fields = ['AssessmentItemNbr','AssessmentItemName','Course','Unit','Weighting'] 
        labels = {'AssessmentItemNbr': "AI Nbr",'AssessmentItemName': "Assessment Item Name",'Course': "Course",'Unit': "Unit",'Weighting': "Weighting (%)",}
        widgets = {
            'AssessmentItemNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Assessment Item Number'}),
            'AssessmentItemName': forms.TextInput(attrs={'class': 'form-control'}),
            'Course': forms.Select(attrs={'class': 'form-control'}),
            'Unit': forms.Select(attrs={'class': 'form-control'}),
            'Weighting': forms.TextInput(attrs={'class': 'form-control'}),
            }

class enrolmentForm(forms.ModelForm):
    class Meta:
        model = tblEnrolment
        fields = ['EnrolmentNbr','EnrolmentDate','EnrolmentName','School','Subject','Course','Unit','Student','StartDate','EndDate'] 
        labels = {'EnrolmentNbr': "Enrol Nbr",'EnrolmentDate': "Enrolment Date",'EnrolmentName': "Enrolment Name",'School': "School",'Subject': "Subject",'Course': "Course",
                  'Unit': "Unit",'Student': "Student",'StartDate': "Start Date",'EndDate': "End Date",}
        widgets = {
            'EnrolmentNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Enrolment Number'}),
            'EnrolmentDate': forms.TextInput(attrs={'class': 'form-control'}),
            'EnrolmentName': forms.TextInput(attrs={'class': 'form-control'}),
            'School': forms.Select(attrs={'class': 'form-control'}),
            'Subject': forms.Select(attrs={'class': 'form-control'}),
            'Course': forms.Select(attrs={'class': 'form-control'}),
            'Unit': forms.Select(attrs={'class': 'form-control'}),
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'StartDate': forms.TextInput(attrs={'class': 'form-control'}),
            'EndDate': forms.TextInput(attrs={'class': 'form-control'}),
            }

class markbookForm(forms.ModelForm):
    class Meta:
        model = tblMarkbook
        fields = ['MarkbookNbr','MarkbookName','Teacher','Course','Unit','AssessmentItem','MarkValue','MarkDate', 'VET']
        labels = {'MarkbookNbr': "Markbook Number   ",'MarkbookName': "Markbook Name       ",'Teacher': "Teacher Name       ",'Course': "Course        ",'Unit': "Unit          ",
                  'AssessmentItem': "Assessment Item     ",'MarkValue': "Mark Value/Weighting (%)",'MarkDate': "Due Date         ",'VET': "VET",}
        widgets = {
            'MarkbookNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Markbook Number'}),
            'MarkbookName': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Markbook Name'}),
            'Teacher': forms.Select(attrs={'class': 'form-control','placeholder': 'Select Teacher'}),
            'Course': forms.Select(attrs={'class': 'form-control','placeholder': 'Select Course'}),
            'Unit': forms.Select(attrs={'class': 'form-control','placeholder': 'Select Unit'}),
            'AssessmentItem': forms.Select(attrs={'class': 'form-control','placeholder': 'Select Assessment Item '}),
            'MarkValue': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Weighting Percentage'}),
            'MarkDate': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Due Date'}),
            'VET': forms.CheckboxInput(attrs={'class': 'form-check-input','placeholder': 'Included in VET?'}),
            }

class submissionForm(forms.ModelForm):
    class Meta:
        model = tblSubmission
        fields = ['SubmissionNbr','SubmissionName','Markbook','Course','Unit','AssessmentItem','Student','SubmissionMark','SubmissionDate']
        labels = {'SubmissionNbr': "Sub Nbr",'SubmissionName': "Submission Name",'Markbook': "Markbook",'Course': "Course",'Unit': "Unit",'AssessmentItem': "Assessment Item",
                  'Student': "Student",'SubmissionMark': "Submission Mark",'SubmissionDate': "Submission Date",}
        widgets = {
            'SubmissionNbr': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Submission Number'}),
            'SubmissionName': forms.TextInput(attrs={'class': 'form-control'}),
            'Markbook': forms.Select(attrs={'class': 'form-control'}),
            'Course': forms.Select(attrs={'class': 'form-control'}),
            'Unit': forms.Select(attrs={'class': 'form-control'}),
            'AssessmentItem': forms.Select(attrs={'class': 'form-control'}),
            'Student': forms.Select(attrs={'class': 'form-control'}),
            'SubmissionMark': forms.TextInput(attrs={'class': 'form-control'}),
            'SubmissionDate': forms.TextInput(attrs={'class': 'form-control'}),
            }


#------------------------------------------------------------------------------------------------------------------------------------------------------




#bootstrap authentication----------------------------------------------------------------------
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
    #--------------------------------------------------------------------------------------------