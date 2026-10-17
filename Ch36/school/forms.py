from django import forms
from .models import Person


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['student_name', 'email', 'password']
        labels = {'student_name': 'Student Name'}
        widgets = {'password': forms.PasswordInput}

    #saves every email in lowercase (TeacherRegistration inherits this too)
    def clean_email(self):
        return self.cleaned_data['email'].lower()


#modelform inheritance: TeacherRegistration gets everything from StudentRegistration
class TeacherRegistration(StudentRegistration):
    #Meta(StudentRegistration.Meta) keeps model and widgets, and changes only fields and labels
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name', 'email', 'password']
        labels = {'teacher_name': 'Teacher Name'}
