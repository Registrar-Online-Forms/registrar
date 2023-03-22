from django.db import models

# new code needs to be migrated 'Python3 manage.py makemigrations' 
# then 'Python3 manage.py migrate'

class User(models.Model):
    #studId = models.CharField(primary_key=True, max_length=8, editable=False, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + ' ' + self.lname


    
