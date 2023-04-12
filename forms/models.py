from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Course(models.Model):
    course_number = models.CharField(max_length=10)
    instructor_name = models.CharField(max_length=50)
    instructor_email = models.EmailField()

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

class AddDropClassForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_signature = models.ImageField(upload_to='signatures/')
    instructor_signature = models.ImageField(upload_to='signatures/')
    additional_approvers_emails = models.TextField(blank=True, null=True)


class AuditToCreditForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    advisor_name = models.CharField(max_length=50)
    advisor_email = models.EmailField()
    student_signature = models.ImageField(upload_to='signatures/')
    instructor_signature = models.ImageField(upload_to='signatures/')
    advisor_signature = models.ImageField(upload_to='signatures/')
    additional_approvers_emails = models.TextField(blank=True, null=True)

class CreditToAuditForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    advisor_name = models.CharField(max_length=50)
    advisor_email = models.EmailField()
    instructor_name = models.CharField(max_length=50)
    instructor_email = models.EmailField()
    advisor_signature = models.ImageField(upload_to='signatures/')
    instructor_signature = models.ImageField(upload_to='signatures/')
    department_chair_name = models.CharField(max_length=50)
    department_chair_email = models.EmailField()
    department_chair_signature = models.ImageField(upload_to='signatures/')
    additional_approvers_emails = models.TextField(blank=True, null=True)

class DeclareMajorForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    student_signature = models.ImageField(upload_to='signatures/')
    student_catalogue_year = models.IntegerField()
    student_anticipted_degree_date = models.DateField()
    student_declared_major = models.BooleanField(default=False)
    department_chair_name = models.CharField(max_length=50)
    department_chair_email = models.EmailField()
    department_chair_signature = models.ImageField(upload_to='signatures/')
    additional_approvers_emails = models.TextField(blank=True, null=True)


class DeclareMinorForm(models.Model):
    form = models.OneToOneField(Form, on_delete=models.CASCADE)
    student_signature = models.ImageField(upload_to='signatures/')
    student_catalogue_year = models.IntegerField()
    student_anticipted_degree_date = models.DateField()
    student_declared_minor = models.BooleanField(default=False)
    department_chair_name = models.CharField(max_length=50)
    department_chair_email = models.EmailField()
    department_chair_signature = models.ImageField(upload_to='signatures/')
    additional_approvers_emails = models.TextField(blank=True, null=True)

    
