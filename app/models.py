from django.db import models

# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.sname

class Course(models.Model):
    sname=models.ForeignKey(Student,on_delete=models.CASCADE)
    cname=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.cname

class Institite(models.Model):
    cname=models.ForeignKey(Course,on_delete=models.CASCADE)
    jdate=models.DateField()