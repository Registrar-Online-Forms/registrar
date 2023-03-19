from django.db import models

class MyModel(models.Model):
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    stu_email = models.EmailField(max_length=8+23)
    stu_ID = models.CharField(max_length=7)
    form_type = models.IntegerField()
    course_code = models.CharField(max_length=11)
    instructor = models.CharField(max_length=50)
    instructor_email = models.EmailField(max_length=50)
    student_signature = models.CharField(max_length=50)
    instructor_signature = models.CharField(max_length=50)
