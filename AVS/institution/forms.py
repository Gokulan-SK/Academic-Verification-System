from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_number', 'name', 'graduation_date', 'enrollment_date', 'course', 'degree', 'degree_certificate', 'transcript']
