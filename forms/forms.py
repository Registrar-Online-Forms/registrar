from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["f_name", "l_name", "stu_email", "stu_ID", "form_type", "course_code", "instructor", "instructor_email", "student_signature", "instructor_signature"]
    labels = {'fname': 'First Name', 'lname': 'Last Name', 'email': 'Email', 'student_id': 'Student ID', 'form_type': 'Form Type', 'course_code': 'Course Code', 'instructor': 'Instructor', 'instructor_email': 'Instructor Email', 'student_signature': 'Student Signature', 'instructor_signature': 'Instructor Signature'}