from django.db import models
from django.contrib.auth.models import User

# Student class stores the basic information of a student
class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

# Course class stores the information about a course
class Course(models.Model):
    course_number = models.CharField(max_length=10)
    instructor_name = models.CharField(max_length=50)
    instructor_email = models.EmailField()

# Form class is the base class for all other forms and stores the information common to all forms
class Form(models.Model):
    PENDING = 'P'
    APPROVED = 'A'
    REJECTED = 'R'
    STATUS_CHOICES = [
        (PENDING, 'Pending Approval'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    form_type = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# AddDropClassForm class stores the information related to a student adding or dropping a course
class AddDropClassForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    additional_approvers_emails = models.TextField(blank=True, null=True)

# AuditToCreditForm class stores the information related to a student converting an audit course to a credit course
class AuditToCreditForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    advisor_name = models.CharField(max_length=50)
    advisor_email = models.EmailField()
    additional_approvers_emails = models.TextField(blank=True, null=True)

# CreditToAuditForm class stores the information related to a student converting a credit course to an audit course
class CreditToAuditForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    advisor_name = models.CharField(max_length=50)
    advisor_email = models.EmailField()
    instructor_name = models.CharField(max_length=50)
    instructor_email = models.EmailField()
    department_chair_name = models.CharField(max_length=50)
    department_chair_email = models.EmailField()
    additional_approvers_emails = models.TextField(blank=True, null=True)

# DeclareMajorForm class stores the information related to a student declaring a major
class DeclareMajorForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    student_catalogue_year = models.IntegerField()
    student_anticipted_degree_date = models.DateField()
    student_declared_major = models.BooleanField(default=False)
    department_chair_name = models.CharField(max_length=50)
    department_chair_email = models.EmailField()
    additional_approvers_emails = models.TextField(blank=True, null=True)

# DeclareMinorForm class stores the information related to a student declaring a minor
class DeclareMinorForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    student_catalogue_year = models.IntegerField()
    student_anticipted_degree_date = models.DateField()
    student_declared_minor = models.BooleanField(default=False)
    department_chair_name = models.CharField(max_length=50)
    department_chair_email = models.EmailField()
    additional_approvers_emails = models.TextField(blank=True, null=True)

    
